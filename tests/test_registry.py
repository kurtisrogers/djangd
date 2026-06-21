import pytest
from django.template import Context, Template

from djangd_framework import Component, register, registry
from djangd_framework.registry import ComponentError


def render(tpl: str, ctx: dict | None = None) -> str:
    return Template("{% load djangd %}" + tpl).render(Context(ctx or {}))


def test_button_renders_label():
    out = render('{% component "button" label="Hi" / %}')
    assert "Hi" in out
    assert "mdc-button" in out
    assert "djangd-button" in out


def test_button_block_children():
    out = render('{% component "button" label="" %}<span>kids</span>{% endcomponent %}')
    assert "<span>kids</span>" in out


def test_self_closing_inside_block():
    out = render(
        '{% component "card" %}{% component "button" label="Save" / %}{% endcomponent %}'
    )
    assert "mdc-card" in out
    assert "Save" in out


def test_required_props_raise():
    with pytest.raises(ComponentError):
        render('{% component "text_field" / %}')  # missing label


def test_unknown_component_raises():
    with pytest.raises(ComponentError):
        render('{% component "does-not-exist" / %}')


def test_register_and_replace():
    class A(Component):
        name = "tests.alpha"
        template = "djangd/components/typography.html"
        defaults = {"text": "alpha", "variant": "body1", "tag": "p"}

    register(A)
    assert "tests.alpha" in registry

    class B(Component):
        name = "tests.alpha"
        template = "djangd/components/typography.html"
        defaults = {"text": "beta", "variant": "body1", "tag": "p"}

    with pytest.raises(ComponentError):
        register(B)
    register(B, replace=True)
    out = render('{% component "tests.alpha" / %}')
    assert "beta" in out


def test_bem_classes_are_present_in_card():
    out = render('{% component "card" outlined=True %}body{% endcomponent %}')
    assert "mdc-card" in out
    assert "mdc-card--outlined" in out
    assert "djangd-card" in out


def test_alert_has_aria_live():
    out = render('{% component "alert" severity="warning" message="Watch out" / %}')
    assert 'role="alert"' in out
    assert 'aria-live="polite"' in out


def test_checkbox_has_label_for_attribute():
    out = render('{% component "checkbox" name="terms" label="Agree" checked=True / %}')
    assert "Agree" in out
    assert 'for="djangd-cb-terms"' in out
