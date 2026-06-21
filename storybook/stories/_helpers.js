/**
 * Mini renderer that mirrors what Django produces for each component.
 *
 * IMPORTANT: This is intentionally a duplicate of the markup in the Django
 * templates — only for Storybook. The *real* source of truth is the Django
 * template (so that what you see in Storybook matches what your Django app
 * renders). Whenever you edit a template under
 * ``djangd_framework/templates/djangd/components/``, mirror the change here.
 *
 * For component contributors: prefer running ``python manage.py
 * djangd_export_stories`` (provided by the example project) which dumps real
 * rendered HTML into ``storybook/public/rendered/`` and lets you iframe it
 * for byte-perfect parity. The hand-written renderers below are a lighter
 * alternative for live controls in Storybook.
 */

export function cls(...parts) {
  return parts.filter(Boolean).join(" ");
}

export function attrs(obj = {}) {
  return Object.entries(obj)
    .filter(([, v]) => v !== false && v !== null && v !== undefined)
    .map(([k, v]) => (v === true ? k : `${k}="${String(v).replace(/"/g, "&quot;")}"`))
    .join(" ");
}
