"""Component registry.

The registry is the single source of truth for djangd-framework components.

A component is defined by subclassing :class:`Component`. Subclasses declare:

* ``name`` — a unique slug used by the ``{% component %}`` template tag.
* ``template`` — the path to the HTML template to render.
* ``defaults`` — default values for props.
* ``allowed_props`` — optional explicit allow-list of prop names; if set, any
  unknown prop will raise an error in DEBUG and be ignored in production.
* ``required_props`` — props that must be supplied at render time.

Components can be extended in two ways:

1. **Override the template** — point the same component name at your own
   template by re-registering, e.g. ``register(MyButton, replace=True)``.
2. **Subclass the component** — extend the Python class to customise prop
   resolution, then register under a new name (e.g. ``"my.button"``).

Custom (non-Material) components register the same way — they automatically
become available as ``{% component "namespace.name" ... %}``.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, ClassVar, Mapping

from django.template.loader import render_to_string
from django.utils.safestring import SafeString, mark_safe


_NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$")


class ComponentError(Exception):
    """Raised for invalid component definitions or usage."""


@dataclass
class _Registration:
    component: type["Component"]
    source: str = "builtin"  # or "user"


class Registry:
    """Global registry mapping component name -> Component class."""

    def __init__(self) -> None:
        self._items: dict[str, _Registration] = {}

    def register(
        self,
        component: type["Component"] | None = None,
        *,
        name: str | None = None,
        replace: bool = False,
        source: str = "user",
    ):
        """Register a component class.

        Can be used as a decorator::

            @registry.register
            class MyAlert(Component):
                name = "my.alert"
                template = "my_app/alert.html"

        Or imperatively::

            registry.register(MyAlert)
        """

        def _do_register(cls: type["Component"]) -> type["Component"]:
            resolved_name = name or cls.name
            if not resolved_name:
                raise ComponentError(
                    f"{cls.__name__} must define a `name` attribute or be "
                    "registered with name=...",
                )
            if not _NAME_RE.match(resolved_name):
                raise ComponentError(
                    f"Invalid component name {resolved_name!r}. Use lowercase "
                    "letters, numbers, dots, dashes or underscores.",
                )
            if resolved_name in self._items and not replace:
                existing = self._items[resolved_name].component
                raise ComponentError(
                    f"Component {resolved_name!r} already registered as "
                    f"{existing.__name__}. Pass replace=True to override.",
                )
            cls.name = resolved_name
            self._items[resolved_name] = _Registration(component=cls, source=source)
            return cls

        if component is None:
            return _do_register
        return _do_register(component)

    def unregister(self, name: str) -> None:
        self._items.pop(name, None)

    def clear(self, *, source: str | None = None) -> None:
        """Remove all registrations (or only those from a given source)."""
        if source is None:
            self._items.clear()
        else:
            for n in [n for n, r in self._items.items() if r.source == source]:
                self._items.pop(n, None)

    def get(self, name: str) -> type["Component"]:
        try:
            return self._items[name].component
        except KeyError as exc:
            raise ComponentError(
                f"No component registered for {name!r}. "
                f"Registered: {sorted(self._items)}",
            ) from exc

    def all(self) -> Mapping[str, type["Component"]]:
        return {n: r.component for n, r in sorted(self._items.items())}

    def by_group(self, group: str) -> list[str]:
        """Names of components in the given group."""
        return sorted(
            n for n, r in self._items.items() if getattr(r.component, "group", "misc") == group
        )

    def groups(self) -> list[str]:
        """All distinct component groups currently in the registry."""
        return sorted({getattr(r.component, "group", "misc") for r in self._items.values()})

    def __contains__(self, name: str) -> bool:
        return name in self._items


registry = Registry()


def register(component: type["Component"] | None = None, **kwargs):
    """Module-level convenience wrapper around ``registry.register``."""
    return registry.register(component, **kwargs)


@dataclass
class Component:
    """Base class for all djangd-framework components.

    Subclasses set class-level attributes describing the component. Instances
    of subclasses are short-lived: one is created per render to validate and
    resolve props, then it is thrown away.

    Components are intentionally lightweight — almost all logic lives in
    Django templates so users can override them easily.
    """

    # ---- declarative attributes (override in subclasses) --------------------
    name: ClassVar[str] = ""
    template: ClassVar[str] = ""
    defaults: ClassVar[dict[str, Any]] = {}
    allowed_props: ClassVar[tuple[str, ...] | None] = None
    required_props: ClassVar[tuple[str, ...]] = ()
    # Logical group the component belongs to ("inputs", "feedback", ...).
    # Used by the tree-shake config and by the CSS subset builder so groups
    # can be opted in/out as a unit. Defaults to "misc".
    group: ClassVar[str] = "misc"
    # The SCSS partial(s) under ``static/djangd/scss/components/`` this
    # component depends on (without the leading underscore or .scss). Used
    # by ``djangd_build_css`` to emit a minimal entry stylesheet.
    scss_partials: ClassVar[tuple[str, ...]] = ()

    # ---- runtime state ------------------------------------------------------
    props: dict[str, Any] = field(default_factory=dict)
    children: str = ""

    # ---- API ----------------------------------------------------------------
    def resolve(self) -> dict[str, Any]:
        """Build the template context. Override to add computed props."""
        ctx: dict[str, Any] = {}
        # Start from defaults (deep copy of dict values to avoid mutation).
        for k, v in self.defaults.items():
            ctx[k] = v
        # Layer caller props on top.
        for k, v in self.props.items():
            ctx[k] = v
        # Children are pre-rendered HTML (either from the {% component %}
        # template tag's nodelist or from a direct Python caller passing
        # rendered child components). Treat them as safe so Django doesn't
        # double-escape the markup. Plain string callers who want escaping
        # should escape upstream — children is by contract "raw HTML".
        ctx["children"] = (
            self.children if isinstance(self.children, SafeString) else mark_safe(self.children or "")
        )
        ctx["_component_name"] = self.name
        # BEM block class — every component gets ``mdc-<block>`` plus our own
        # ``djangd-<block>`` hook for override-only styles.
        block = ctx.get("block") or self.name.split(".")[-1]
        ctx["block"] = block
        ctx.setdefault("extra_classes", "")
        ctx.setdefault("attrs", {})
        ctx.setdefault("id", None)
        return ctx

    def validate(self) -> None:
        """Verify required props are present and no unknown props are passed."""
        missing = [p for p in self.required_props if p not in self.props]
        if missing:
            raise ComponentError(
                f"Component {self.name!r} missing required prop(s): "
                f"{', '.join(missing)}",
            )
        if self.allowed_props is not None:
            allowed = set(self.allowed_props) | set(self.defaults) | {
                "block",
                "extra_classes",
                "attrs",
                "id",
            }
            unknown = [p for p in self.props if p not in allowed]
            if unknown:
                from django.conf import settings

                msg = (
                    f"Component {self.name!r} received unknown prop(s): "
                    f"{', '.join(unknown)}"
                )
                if getattr(settings, "DEBUG", False):
                    raise ComponentError(msg)

    def render(self) -> str:
        self.validate()
        if not self.template:
            raise ComponentError(
                f"Component {self.name!r} ({type(self).__name__}) defines no "
                "`template`.",
            )
        return render_to_string(self.template, self.resolve())
