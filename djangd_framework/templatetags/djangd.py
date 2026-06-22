"""Template tags for rendering djangd-framework components.

Usage in any Django template::

    {% load djangd %}

    {# Self-closing (no children). Note the trailing slash. #}
    {% component "button" label="Save" variant="raised" / %}

    {# Block form with children #}
    {% component "card" elevated=True %}
        <h2>Title</h2>
        <p>Body</p>
    {% endcomponent %}

    {# Pass an explicit ``id`` and arbitrary HTML attributes #}
    {% component "text_field" label="Email" id="id_email" attrs=email_attrs / %}

The explicit ``/`` is required for self-closing components — it lets us
disambiguate self-closing tags nested inside block components.
"""
from __future__ import annotations

from django import template
from django.template.base import Node, NodeList, Parser, Token, TemplateSyntaxError
from django.utils.html import escape
from django.utils.safestring import mark_safe

from ..registry import registry

register = template.Library()


class ComponentNode(Node):
    def __init__(
        self,
        name_var,
        kwargs: dict[str, template.base.FilterExpression],
        nodelist: NodeList | None,
    ):
        self.name_var = name_var
        self.kwargs = kwargs
        self.nodelist = nodelist

    def render(self, context) -> str:
        name = self.name_var.resolve(context)
        resolved = {k: v.resolve(context) for k, v in self.kwargs.items()}
        children = ""
        if self.nodelist is not None:
            children = self.nodelist.render(context)
        component_cls = registry.get(name)
        component = component_cls(props=resolved, children=children)
        return mark_safe(component.render())  # noqa: S308


def _parse_kwargs(parser: Parser, bits: list[str]) -> dict[str, template.base.FilterExpression]:
    kwargs: dict[str, template.base.FilterExpression] = {}
    for bit in bits:
        if "=" not in bit:
            raise TemplateSyntaxError(
                f"Unexpected positional argument {bit!r} to {{% component %}}; "
                "all arguments after the component name must be keyword args."
            )
        key, _, raw_value = bit.partition("=")
        kwargs[key] = parser.compile_filter(raw_value)
    return kwargs


@register.tag(name="component")
def do_component(parser: Parser, token: Token) -> ComponentNode:
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError(
            "{% component %} requires a component name as its first argument."
        )
    tag_name, name_arg, *kwarg_bits = bits
    name_var = parser.compile_filter(name_arg)

    self_closing = False
    if kwarg_bits and kwarg_bits[-1] == "/":
        self_closing = True
        kwarg_bits = kwarg_bits[:-1]

    kwargs = _parse_kwargs(parser, kwarg_bits)

    nodelist: NodeList | None = None
    if not self_closing:
        end_token = f"end{tag_name}"
        nodelist = parser.parse((end_token,))
        parser.delete_first_token()
    return ComponentNode(name_var, kwargs, nodelist)


@register.simple_tag(name="djangd_assets")
def djangd_assets(include_js: bool = True) -> str:
    """Renders the CSS (and optionally JS) ``<link>``/``<script>`` tags.

    Drop ``{% djangd_assets %}`` into your base template's ``<head>``.
    """
    css = (
        '<link rel="stylesheet" '
        'href="/static/djangd/dist/djangd.css" />'
    )
    js = ""
    if include_js:
        js = (
            '<script defer src="/static/djangd/dist/djangd.js"></script>'
        )
    return mark_safe(css + js)  # noqa: S308


@register.filter(name="djangd_attrs")
def djangd_attrs(value: dict | None) -> str:
    """Render a dict as HTML attributes, safely.

    Used inside component templates: ``{{ attrs|djangd_attrs }}``.
    """
    if not value:
        return ""
    parts: list[str] = []
    for k, v in value.items():
        if v is True:
            parts.append(escape(k))
        elif v is False or v is None:
            continue
        else:
            parts.append(f'{escape(k)}="{escape(v)}"')
    return mark_safe(" ".join(parts))  # noqa: S308


@register.filter(name="djangd_sub")
def djangd_sub(value, arg) -> int:
    """Subtract ``arg`` from ``value`` (both coerced to int).

    Used in templates where a numeric subtraction is needed and Django's
    built-in ``add`` filter can't compose because the operand is a variable.
    """
    try:
        return int(value) - int(arg)
    except (TypeError, ValueError):
        return value
