"""Built-in Material components, registered on app ready.

Every component is a thin subclass of :class:`djangd_framework.Component`
that points at a BEM-styled template under ``templates/djangd/components/``.

The registrations here form the **single source of truth** for the
component library — adding a new built-in component just means creating a
template, a class here, and a story under ``storybook/stories/``.

To extend or override any component in user code::

    from djangd_framework import Component, register

    @register(replace=True)
    class Button(Component):
        name = "button"
        template = "myapp/button.html"  # your own template

Or to add a brand-new component::

    @register
    class Alert(Component):
        name = "myapp.alert"
        template = "myapp/alert.html"
        defaults = {"severity": "info"}
        required_props = ("message",)
"""
from __future__ import annotations

from typing import ClassVar

from ..registry import Component, register

# A compact metaclass-free way to declare lots of similar components.


def _make(
    name: str,
    template: str,
    defaults: dict | None = None,
    allowed: tuple[str, ...] | None = None,
    required: tuple[str, ...] = (),
) -> type[Component]:
    cls = type(
        f"{name.replace('.', '_').title()}Component",
        (Component,),
        {
            "name": name,
            "template": template,
            "defaults": dict(defaults or {}),
            "allowed_props": allowed,
            "required_props": required,
        },
    )
    return register(cls, source="builtin")


# ---------------------------------------------------------------------------
# Inputs & actions
# ---------------------------------------------------------------------------
_make(
    "button",
    "djangd/components/button.html",
    defaults={
        "label": "",
        "variant": "text",  # text | outlined | raised | unelevated
        "type": "button",
        "disabled": False,
        "icon": None,
        "trailing_icon": False,
        "href": None,
        "size": "medium",  # small | medium | large
    },
    required=("label",),
)
_make(
    "icon_button",
    "djangd/components/icon_button.html",
    defaults={"icon": "favorite", "label": "", "toggled": False, "disabled": False},
    required=("icon", "label"),
)
_make(
    "fab",
    "djangd/components/fab.html",
    defaults={"icon": "add", "label": "", "extended": False, "mini": False, "exited": False},
    required=("icon", "label"),
)
_make(
    "chip",
    "djangd/components/chip.html",
    defaults={"label": "", "icon": None, "trailing_icon": None, "selected": False, "removable": False},
    required=("label",),
)
_make(
    "text_field",
    "djangd/components/text_field.html",
    defaults={
        "variant": "filled",  # filled | outlined
        "label": "",
        "name": "",
        "value": "",
        "type": "text",
        "placeholder": "",
        "helper": "",
        "error": False,
        "required": False,
        "disabled": False,
        "leading_icon": None,
        "trailing_icon": None,
        "id": None,
        "rows": None,  # if set, renders <textarea>
    },
    required=("label",),
)
_make(
    "checkbox",
    "djangd/components/checkbox.html",
    defaults={"label": "", "name": "", "value": "1", "checked": False, "disabled": False, "indeterminate": False, "id": None},
)
_make(
    "radio",
    "djangd/components/radio.html",
    defaults={"label": "", "name": "", "value": "", "checked": False, "disabled": False, "id": None},
    required=("name", "value"),
)
_make(
    "switch",
    "djangd/components/switch.html",
    defaults={"label": "", "name": "", "checked": False, "disabled": False, "id": None},
)
_make(
    "select",
    "djangd/components/select.html",
    defaults={"label": "", "name": "", "options": (), "value": "", "variant": "filled", "helper": "", "required": False, "disabled": False, "id": None},
    required=("label", "options"),
)
_make(
    "slider",
    "djangd/components/slider.html",
    defaults={"label": "", "name": "", "min": 0, "max": 100, "step": 1, "value": 50, "discrete": False, "disabled": False, "id": None},
)
_make(
    "form_field",
    "djangd/components/form_field.html",
    defaults={"label": "", "align_end": False},
)

# ---------------------------------------------------------------------------
# Surfaces
# ---------------------------------------------------------------------------
_make(
    "card",
    "djangd/components/card.html",
    defaults={"outlined": False, "media": None, "media_alt": "", "actions": None},
)
_make(
    "paper",
    "djangd/components/paper.html",
    defaults={"elevation": 1},
)
_make(
    "divider",
    "djangd/components/divider.html",
    defaults={"inset": False, "padded": False, "orientation": "horizontal"},
)
_make(
    "elevation",
    "djangd/components/elevation.html",
    defaults={"level": 1},
)

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
_make(
    "app_bar",
    "djangd/components/app_bar.html",
    defaults={
        "title": "",
        "variant": "standard",  # standard | short | short-collapsed | fixed | prominent | dense
        "navigation_icon": "menu",
        "navigation_label": "Open navigation menu",
        "actions": (),
    },
)
_make(
    "drawer",
    "djangd/components/drawer.html",
    defaults={
        "title": "",
        "subtitle": "",
        "variant": "permanent",  # permanent | dismissible | modal
        "open": True,
        "items": (),
    },
)
_make(
    "tab_bar",
    "djangd/components/tab_bar.html",
    defaults={"tabs": (), "active": 0, "stacked": False, "min_width": False},
    required=("tabs",),
)
_make(
    "bottom_navigation",
    "djangd/components/bottom_navigation.html",
    defaults={"items": (), "active": 0},
    required=("items",),
)
_make(
    "menu",
    "djangd/components/menu.html",
    defaults={"items": (), "open": False, "id": None},
    required=("items",),
)
_make(
    "breadcrumbs",
    "djangd/components/breadcrumbs.html",
    defaults={"items": (), "separator": "/"},
    required=("items",),
)
_make(
    "pagination",
    "djangd/components/pagination.html",
    defaults={"page": 1, "total": 1, "url": "?page="},
)

# ---------------------------------------------------------------------------
# Data display
# ---------------------------------------------------------------------------
_make(
    "list",
    "djangd/components/list.html",
    defaults={"items": (), "two_line": False, "avatar_list": False, "dense": False, "non_interactive": False},
    required=("items",),
)
_make(
    "table",
    "djangd/components/table.html",
    defaults={"columns": (), "rows": (), "caption": "", "sticky_header": False},
    required=("columns", "rows"),
)
_make(
    "avatar",
    "djangd/components/avatar.html",
    defaults={"src": None, "alt": "", "initials": "", "size": "medium", "shape": "circle"},
)
_make(
    "badge",
    "djangd/components/badge.html",
    defaults={"value": "", "max": 99, "dot": False, "color": "primary"},
)
_make(
    "tooltip",
    "djangd/components/tooltip.html",
    defaults={"text": "", "id": None, "position": "top"},
    required=("text",),
)
_make(
    "typography",
    "djangd/components/typography.html",
    defaults={"variant": "body1", "tag": None, "text": "", "align": None, "color": None, "no_wrap": False},
)

# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------
_make(
    "alert",
    "djangd/components/alert.html",
    defaults={"severity": "info", "title": "", "message": "", "dismissible": False, "icon": None},
)
_make(
    "snackbar",
    "djangd/components/snackbar.html",
    defaults={"message": "", "action_label": "", "leading": False, "stacked": False, "id": None},
    required=("message",),
)
_make(
    "dialog",
    "djangd/components/dialog.html",
    defaults={"title": "", "scrim_click_action": "close", "escape_key_action": "close", "actions": (), "id": None},
)
_make(
    "linear_progress",
    "djangd/components/linear_progress.html",
    defaults={"value": None, "buffer": None, "indeterminate": True, "label": "Loading"},
)
_make(
    "circular_progress",
    "djangd/components/circular_progress.html",
    defaults={"value": None, "indeterminate": True, "label": "Loading", "size": "medium"},
)
_make(
    "skeleton",
    "djangd/components/skeleton.html",
    defaults={"variant": "text", "width": None, "height": None, "lines": 1, "animation": "pulse"},
)

# ---------------------------------------------------------------------------
# Misc / utility
# ---------------------------------------------------------------------------
_make(
    "icon",
    "djangd/components/icon.html",
    defaults={"name": "", "label": "", "size": None},
    required=("name",),
)
_make(
    "image_list",
    "djangd/components/image_list.html",
    defaults={"items": (), "masonry": False, "with_text": False},
    required=("items",),
)
_make(
    "stepper",
    "djangd/components/stepper.html",
    defaults={"steps": (), "active": 0, "orientation": "horizontal"},
    required=("steps",),
)
_make(
    "accordion",
    "djangd/components/accordion.html",
    defaults={"items": (), "exclusive": False},
    required=("items",),
)
_make(
    "speed_dial",
    "djangd/components/speed_dial.html",
    defaults={"icon": "add", "label": "", "actions": ()},
    required=("actions",),
)
_make(
    "rating",
    "djangd/components/rating.html",
    defaults={"value": 0, "max": 5, "readonly": False, "name": "rating", "label": "Rating"},
)
_make(
    "toggle_button_group",
    "djangd/components/toggle_button_group.html",
    defaults={"items": (), "value": None, "name": "toggle", "exclusive": True},
    required=("items",),
)
_make(
    "container",
    "djangd/components/container.html",
    defaults={"max_width": "lg", "fluid": False, "padded": True},
)
_make(
    "grid",
    "djangd/components/grid.html",
    defaults={"columns": 12, "gap": "md", "items": ()},
)
_make(
    "stack",
    "djangd/components/stack.html",
    defaults={"direction": "vertical", "gap": "md", "align": None, "justify": None, "items": ()},
)
_make(
    "box",
    "djangd/components/box.html",
    defaults={
        "tag": "div",
        "padding": None,   # 0..6 | None — maps to djangd-box--p-<n>
        "margin": None,    # 0..6 | "auto" | None — maps to djangd-box--m-<n>
        "display": None,   # block | inline | inline-block | flex | inline-flex | grid | hidden | None
        "align": None,     # start | center | end | stretch | None
        "justify": None,   # start | center | end | between | around | None
        "rounded": None,   # xs | sm | md | lg | pill | None
        "surface": None,   # default | variant | primary | None
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Inputs (extended): autocomplete, button group, transfer list
# ---------------------------------------------------------------------------
_make(
    "autocomplete",
    "djangd/components/autocomplete.html",
    defaults={
        "label": "",
        "name": "",
        "value": "",
        "options": (),   # iterable of strings, or dicts: {"value": ..., "label": ...}
        "placeholder": "",
        "helper": "",
        "required": False,
        "disabled": False,
        "id": None,
    },
    required=("label", "name"),
)
_make(
    "button_group",
    "djangd/components/button_group.html",
    defaults={
        "buttons": (),       # iterable of pre-rendered button HTML strings
        "label": "",         # accessible group label
        "orientation": "horizontal",  # horizontal | vertical
        "variant": "contained",       # contained | outlined
        "full_width": False,
        "id": None,
    },
)
_make(
    "transfer_list",
    "djangd/components/transfer_list.html",
    defaults={
        "name": "transfer",
        "label": "",
        "source_title": "Available",
        "target_title": "Selected",
        "source_items": (),  # iterable of strings or {"value": ..., "label": ...}
        "target_items": (),  # iterable of strings or {"value": ..., "label": ...}
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Overlays: backdrop, modal, popover
# ---------------------------------------------------------------------------
_make(
    "backdrop",
    "djangd/components/backdrop.html",
    defaults={"open": False, "invisible": False, "id": None},
)
_make(
    "modal",
    "djangd/components/modal.html",
    defaults={
        "open": False,
        "label": "",
        "labelledby": "",
        "describedby": "",
        "id": None,
    },
)
_make(
    "popover",
    "djangd/components/popover.html",
    defaults={
        "open": False,
        "placement": "bottom",  # top | bottom | left | right
        "anchor": None,         # CSS selector or element id the popover is anchored to
        "arrow": True,
        "label": "",
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Link
# ---------------------------------------------------------------------------
_make(
    "link",
    "djangd/components/link.html",
    defaults={
        "text": "",
        "href": "#",
        "target": None,        # _self | _blank | _parent | _top | None
        "variant": "body",     # body | button | inherit
        "underline": "always", # always | hover | none
        "color": "primary",    # primary | secondary | error | success | warning | inherit
        "id": None,
    },
    required=("href",),
)
