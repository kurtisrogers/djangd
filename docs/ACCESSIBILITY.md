# Accessibility (WCAG 2.1 AA)

djangd-framework targets the **AA** level of WCAG 2.1. Each component has
been designed with the following guarantees, which form the test bed for all
contributions.

## Built-in guarantees

| Guarantee | How it is enforced |
|---|---|
| **1.4.3 Contrast (minimum)** — text 4.5:1, UI 3:1 | Default tokens hit AA on light and dark themes. Storybook runs `addon-a11y` (uses `axe-core`) on every render. |
| **1.4.11 Non-text contrast** | Focus rings are 3px solid `currentColor` against the background. |
| **2.1.1 Keyboard** | No interactive element relies on `pointer`/`hover`. Tab order is the DOM order. Tab bar supports ⇦/⇨. |
| **2.4.7 Focus visible** | All interactive blocks scope `:focus-visible` to the framework's focus ring. |
| **2.5.5 Target size** | Buttons/icons default to a 40px hit area; FABs are 56px. |
| **3.3.1 Error identification** | Text fields render an `aria-describedby` helper that flips to `mdc-text-field-helper-text--validation-msg` and red on `error=True`. |
| **3.3.3 Suggestion** | Helper text is reserved for guidance and validation messages. |
| **4.1.2 Name, role, value** | Every interactive component sets the right ARIA role (`role="alert"`, `role="dialog"`, `role="tablist"`, `role="switch"`, etc.) and pairs labels with controls. |
| **2.3.3 Animation from interactions** | All transitions respect `prefers-reduced-motion: reduce`. |

## When you override

When you override a component, the test harness in `tests/test_components.py`
will still smoke-test that it renders, but you are responsible for keeping the
accessibility guarantees above. Two minimum checks:

1. Keep the ARIA roles, labels, and `aria-*` props that the original template
   set.
2. If you change colours, run `npm run storybook` and inspect the **A11y**
   panel — any AA failures show up immediately.

## Auditing your build

We recommend running [`axe-core`](https://github.com/dequelabs/axe-core) or
[`pa11y`](https://pa11y.org/) in CI against pages that use djangd-framework
components — the framework gets you to AA on its own components, but page-level
issues (heading order, alt text on user content) still need their own checks.
