# djangd-framework

A **Django component library** built on **Material Design** primitives.

> Drop-in components for Django templates, with BEM class names, WCAG 2.1 AA
> defaults, full CSS-custom-property theming, and a small registry that lets
> any downstream app override built-ins or register entirely new components.

[![Storybook](https://img.shields.io/badge/Storybook-online-ff4785)](https://kurtisrogers.github.io/djangd/)

---

## Why this design (and why not MUI directly)

You asked for Material UI as the base. **Material UI is React-only** — it
doesn't render in Django templates without a Node/React build pipeline. The
canonical Material Design implementation for **vanilla HTML/CSS/JS** is
[Material Components for the Web (MDC Web)](https://github.com/material-components/material-components-web),
which:

- Implements every Material component you'd reach for in MUI.
- Already uses **BEM** (`.mdc-button__label`, `.mdc-card--outlined`).
- Ships fully-themable Sass and is **WCAG 2.1 AA** compliant out of the box.

djangd-framework wraps MDC's BEM markup in **Django template components**, adds
its own `djangd-` BEM hook so users can layer overrides safely, and exposes
*everything* through CSS custom properties so retheming requires no Sass build.

If you really want React MUI inside a Django page, see
[Alternative approaches](#alternative-approaches) below.

---

## Install

```bash
pip install djangd-framework
```

Add it (and `django-pattern-library`) to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # …
    "djangd_framework",
    "pattern_library",  # optional, for the in-Django pattern library UI
]
```

In your base template:

```django
{% load djangd %}
<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  {% djangd_assets %}    {# emits djangd.css + djangd.js #}
</head>
```

---

## Use a component

```django
{% load djangd %}

{# Self-closing — note the trailing slash #}
{% component "button" label="Save" variant="raised" icon="save" / %}

{# Block form with children — provides an {% endcomponent %} closer #}
{% component "card" outlined=True %}
  {% component "typography" variant="title-large" tag="h2" text="Hello" / %}
  <p>Drop in any HTML — the card is the surface.</p>
{% endcomponent %}
```

Every component supports:

| Prop          | Purpose                                                            |
|---------------|--------------------------------------------------------------------|
| `id`          | Forwarded to the root element                                     |
| `extra_classes` | Appended to the root element's class list                       |
| `attrs`       | Dict of arbitrary HTML attributes (`data-*`, `aria-*`, etc.)      |

Component-specific props are documented in Storybook.

---

## Built-in components

Inputs & actions: `button`, `icon_button`, `fab`, `chip`, `text_field`,
`checkbox`, `radio`, `switch`, `select`, `slider`, `form_field`,
`toggle_button_group`, `rating`

Surfaces: `card`, `paper`, `divider`, `elevation`

Navigation: `app_bar`, `drawer`, `tab_bar`, `bottom_navigation`, `menu`,
`breadcrumbs`, `pagination`

Data display: `list`, `table`, `avatar`, `badge`, `tooltip`, `typography`,
`image_list`

Feedback: `alert`, `snackbar`, `dialog`, `linear_progress`,
`circular_progress`, `skeleton`

Layout & misc: `container`, `grid`, `stack`, `icon`, `stepper`, `accordion`,
`speed_dial`

---

## Theming

The framework only sets CSS custom properties; override any of them anywhere:

```css
:root {
  --djangd-color-primary: #c2185b;
  --djangd-radius-md: 4px;
  --djangd-font-family: "Inter", sans-serif;
}

/* Scoped to a single region */
.marketing { --djangd-color-primary: #2e7d32; }
```

Dark mode is built-in: add `data-djangd-theme="dark"` on `<html>` (or any
wrapper element).

Full token list lives in
[`djangd_framework/static/djangd/scss/abstracts/_tokens.scss`](djangd_framework/static/djangd/scss/abstracts/_tokens.scss).

### Overriding a component's styles

Every component is a BEM block prefixed with `.djangd-`:

```css
/* Bigger, square card with a brand accent border */
.djangd-card {
  border-radius: 0;
  border: 2px solid var(--djangd-color-primary);
}

/* A modifier you can apply on the call site */
.djangd-card--marketing .djangd-card__content { padding: 48px; }
```

```django
{% component "card" extra_classes="djangd-card--marketing" %}…{% endcomponent %}
```

---

## Extending: register a custom component

```python
# my_app/components.py
from djangd_framework import Component, register

@register
class Alert(Component):
    name = "my.alert"
    template = "my_app/alert.html"
    defaults = {"severity": "info", "dismissible": False}
    required_props = ("message",)
    allowed_props = ("message", "severity", "title", "dismissible")
```

Then anywhere in your templates:

```django
{% component "my.alert" severity="warning" message="Server is restarting." dismissible=True %}
```

### Overriding a built-in

```python
@register(replace=True)
class Button(Component):
    name = "button"           # same name as the built-in
    template = "my_app/button.html"
```

Every existing call site keeps working with your markup.

### Custom interactive behaviour

Add JS without a build step:

```html
<script>
  djangd.registerEnhancer("my-tooltip", function (root) {
    root.addEventListener("focusin", () => root.setAttribute("data-show", ""));
    root.addEventListener("focusout", () => root.removeAttribute("data-show"));
  });
</script>
```

The framework auto-runs enhancers on `DOMContentLoaded` and you can call
`djangd.enhance(scope)` after injecting markup dynamically (e.g. via HTMX).

---

## Accessibility

Defaults that ship in every component:

- Visible focus rings (`outline: 3px solid currentColor` with 2px offset).
- ARIA roles, labels, and states on every interactive element.
- `prefers-reduced-motion` automatically silences transitions/animations.
- `color-mix`/CSS-vars-based palette designed to meet WCAG 2.1 **AA**
  contrast for both light and dark themes.
- Form inputs always pair a visible `<label>` with the control.

Storybook ships the `@storybook/addon-a11y` plugin so every story is scanned
on render — the build will surface contrast issues if you retheme too far.

---

## Storybook

```bash
cd storybook
npm install
npm run storybook         # http://localhost:6006
npm run build             # → ../docs/storybook
```

Stories are JavaScript so the dev loop is fast; the same markup is mirrored
from the Django templates. On every push to `main`/`develop`, the
[`.github/workflows/storybook.yml`](.github/workflows/storybook.yml) workflow
builds and deploys to **GitHub Pages**.

### django-pattern-library

The example project also wires up
[`django-pattern-library`](https://torchbox.github.io/django-pattern-library/)
so you can browse the components from inside a running Django app at
`/pattern-library/`.

---

## Example app

```bash
pip install -e ".[dev]"
python example/manage.py runserver
```

Open <http://localhost:8000/> for the demo and <http://localhost:8000/pattern-library/>
for the in-Django component browser.

---

## Tests

```bash
pip install -e ".[dev]"
pytest
```

---

## Alternative approaches

Three other shapes this library could have taken — happy to switch to one if
your needs lean differently:

| Approach | Pros | Cons |
|---|---|---|
| **MDC Web wrappers (what this lib does)** | No Node build needed in your Django project, pure HTML/CSS, BEM out of the box, theming via CSS variables, easy to override per-page. | Some MDC components need ~50 lines of JS for full interactivity (already provided). |
| **Real MUI via `django-react-templatetags`** | Reuses the React MUI ecosystem 1:1. | Requires a Node toolchain and an SSR/hydration story; props pass through a JSON bridge; hard to drop "sections of code in places". |
| **Tailwind + headless primitives (Radix, Headless UI)** | Maximum styling flexibility, no Material lock-in. | You lose the Material look-and-feel until you rebuild it; not what you asked for. |
| **Custom CSS framework + Django includes** | Minimal dependencies. | You rebuild Material from scratch (months of work) and re-invent BEM/a11y conventions. |

The current choice is the best fit for "drop sections of code in places with a
single source of truth" plus all of Material.

---

## License

MIT
