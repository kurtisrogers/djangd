"""Render every Storybook variant via the real Django templates.

Storybook stories load their HTML from ``storybook/public/rendered/<id>.html``
which is produced by running this script. Doing it this way means the
component templates under ``djangd_framework/templates/djangd/components/``
are the single source of truth for what Storybook shows — no hand-mirrored
markup in the ``.stories.js`` files.

The variants are declared in ``storybook/variants.py`` as a mapping of
``"<story-id>" -> ("<component name>", {props})`` (or, for compositions that
combine multiple components, ``("__html__", "literal html string")``).

Run it manually via::

    python storybook/scripts/render.py

…or via the npm ``render:stories`` script. The Storybook ``build`` and ``dev``
scripts chain it automatically.
"""
from __future__ import annotations

import sys
from importlib import import_module
from pathlib import Path

import django
from django.conf import settings


ROOT = Path(__file__).resolve().parents[2]
STORYBOOK_DIR = ROOT / "storybook"
OUT_DIR = STORYBOOK_DIR / "public" / "rendered"


def _configure_django() -> None:
    if settings.configured:
        return
    settings.configure(
        DEBUG=False,
        INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth", "djangd_framework"],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "OPTIONS": {"context_processors": []},
            }
        ],
        USE_TZ=True,
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )
    django.setup()


def main() -> int:
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(STORYBOOK_DIR))

    _configure_django()

    # Importing this module registers every built-in component on the registry.
    import djangd_framework.components  # noqa: F401
    from djangd_framework.registry import registry

    variants_module = import_module("variants")
    variants: dict[str, tuple] = variants_module.VARIANTS

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Wipe stale renders so removed variants don't linger in deploys.
    for stale in OUT_DIR.glob("*.html"):
        stale.unlink()

    written = 0
    for variant_id, spec in variants.items():
        component_name, payload = spec
        if component_name == "__html__":
            # Free-form HTML composition that doesn't map to a single component.
            html = payload
        else:
            cls = registry.get(component_name)
            children = payload.pop("__children__", "") if isinstance(payload, dict) else ""
            html = cls(props=dict(payload), children=children).render()
        (OUT_DIR / f"{variant_id}.html").write_text(html, encoding="utf-8")
        written += 1

    print(f"djangd_export_stories: wrote {written} HTML files to {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
