# Extending djangd-framework

There are four levels of customisation, from light to heavy:

## 1. Re-skin via CSS custom properties (no Python)

Override the `--djangd-*` properties anywhere. Scope to `:root`, a single
component instance via `extra_classes`, or a region.

```css
:root { --djangd-color-primary: #c2185b; --djangd-radius-md: 4px; }
```

## 2. Override component styles (no Python)

Component class names follow strict BEM:

```
.djangd-<block>             /* root */
.djangd-<block>__<element>  /* child elements */
.djangd-<block>--<modifier> /* variants */
```

Target them in your own stylesheet. The framework's selectors are single-class
and low specificity so your overrides win.

## 3. Override a built-in template (Python, one-liner)

Re-register the component name with your own template:

```python
# my_app/components.py
from djangd_framework import Component, register

@register(replace=True)
class Button(Component):
    name = "button"
    template = "my_app/button.html"
```

`my_app/button.html` receives the same context (`label`, `variant`, …) so all
existing call sites keep working.

## 4. Add a brand-new component (Python + template)

```python
@register
class Alert(Component):
    name = "my.alert"
    template = "my_app/alert.html"
    defaults = {"severity": "info", "dismissible": False}
    required_props = ("message",)
    allowed_props = ("message", "severity", "title", "dismissible")

    def resolve(self):
        ctx = super().resolve()
        ctx["icon"] = {"info": "info", "success": "check_circle",
                       "warning": "warning", "error": "error"}[ctx["severity"]]
        return ctx
```

Use it:

```django
{% component "my.alert" severity="warning" message="Heads up" %}
```

## Discovery

Built-ins are registered in `djangd_framework.components` on app ready. For
your own components, either:

- Put them in `your_app/components.py` and trigger import in `AppConfig.ready`
  (see `example/example_app/apps.py`); **or**
- Put them in any module Django imports (e.g. `apps.py`, `models.py`).

## Registry API

```python
from djangd_framework import registry

registry.all()             # {name: ComponentClass}
registry.get("button")     # ComponentClass
registry.register(MyCls)
registry.unregister("button")
"button" in registry       # bool
```

## Validating props

Set `allowed_props` (a tuple) to enable strict prop validation. In DEBUG,
unknown props raise; in production they're silently dropped. Useful while
refactoring.
