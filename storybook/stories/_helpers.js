/**
 * Stories load Django-rendered HTML produced by ``storybook/scripts/render.py``.
 *
 * The component templates under ``djangd_framework/templates/djangd/components/``
 * are the single source of truth for what Storybook renders. The render script
 * walks every variant declared in ``storybook/variants.py``, calls each
 * component class via the registry, and writes the output to
 * ``storybook/public/rendered/<variant-id>.html``. Storybook serves that
 * folder as a static dir, so stories can fetch their HTML by id.
 *
 * Both ``npm run storybook`` and ``npm run build`` chain ``render:stories``
 * automatically, so the rendered files stay in sync with the templates.
 */

const RENDERED_BASE = "rendered";
const cache = new Map();

function loadRendered(variantId) {
  if (!cache.has(variantId)) {
    cache.set(
      variantId,
      fetch(`${RENDERED_BASE}/${variantId}.html`).then((r) => {
        if (!r.ok) {
          throw new Error(
            `Missing rendered variant '${variantId}' — declare it in storybook/variants.py and re-run \`npm run render:stories\`.`
          );
        }
        return r.text();
      })
    );
  }
  return cache.get(variantId);
}

/**
 * Storybook's HTML framework expects ``render()`` to return a string or a
 * DOM Node synchronously — Promises slip past the renderer's type check
 * and produce 'Expecting an HTML snippet or DOM node' errors. So we return
 * a host ``<div>`` immediately and fill its ``innerHTML`` once the fetch
 * resolves.
 */
function makeHost(variantId) {
  const host = document.createElement("div");
  host.className = "djangd-story-host";
  host.dataset.djangdVariant = variantId;

  loadRendered(variantId)
    .then((html) => {
      host.innerHTML = html;
      const djangd = typeof window !== "undefined" ? window.djangd : null;
      if (djangd && typeof djangd.enhance === "function") {
        djangd.enhance(host);
      }
    })
    .catch((err) => {
      host.innerHTML = `<pre style="color:var(--djangd-color-error,#b3261e);background:var(--djangd-color-surface-variant,#fbeff2);padding:12px 16px;border-radius:8px;font-family:var(--djangd-font-family-mono,ui-monospace,monospace);white-space:pre-wrap;">${err.message}</pre>`;
    });

  return host;
}

/**
 * Story that always renders a single Django-rendered variant.
 *
 * @example
 *   export const Raised = djangoStory("button__raised");
 */
export function djangoStory(variantId, extras = {}) {
  return {
    ...extras,
    render: () => makeHost(variantId),
  };
}

/**
 * Story whose argTypes control which Django-rendered variant is shown.
 *
 * Pass a function that maps the resolved args to a variant id; Storybook's
 * controls will swap between the pre-rendered HTML files.
 *
 * @example
 *   export const Default = djangoStoryWithControls({
 *     args: { variant: "raised" },
 *     argTypes: { variant: { control: "select", options: ["raised","outlined","text"] } },
 *     resolve: ({ variant }) => `button__${variant}`,
 *   });
 */
export function djangoStoryWithControls({ args = {}, argTypes = {}, resolve }) {
  return {
    args,
    argTypes,
    render: (resolvedArgs) => makeHost(resolve(resolvedArgs)),
  };
}

/** Join CSS class names, dropping falsy entries. Kept for any composed
 *  demos that still build markup around the rendered components. */
export function cls(...parts) {
  return parts.filter(Boolean).join(" ");
}
