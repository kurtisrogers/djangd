"""Demo: defining and overriding components in a downstream Django app."""
from djangd_framework import Component, register


@register
class HeroCard(Component):
    """A custom marketing hero card built on top of djangd-framework primitives."""

    name = "example.hero_card"
    template = "example_app/hero_card.html"
    defaults = {"title": "", "subtitle": "", "cta_label": "Learn more", "cta_href": "#"}
    required_props = ("title",)
