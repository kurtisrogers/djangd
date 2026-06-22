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

async function loadRendered(variantId) {
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
 * Story that always renders a single Django-rendered variant.
 *
 * @example
 *   export const Raised = djangoStory("button__raised");
 */
export function djangoStory(variantId, extras = {}) {
  return {
    ...extras,
    render: () => loadRendered(variantId),
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
    render: (resolvedArgs) => loadRendered(resolve(resolvedArgs)),
  };
}

/** Join CSS class names, dropping falsy entries. Used by the few stories that
 *  still build composed demos around the rendered components. */
export function cls(...parts) {
  return parts.filter(Boolean).join(" ");
}
