"""Settings for the djangd-framework example/demo project."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "insecure-example-only"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.staticfiles",
    "djangd_framework",
    "example_app",
    "pattern_library",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "example_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": ["pattern_library.loader_tags"],
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

STATIC_URL = "/static/"
STATICFILES_DIRS = []

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PATTERN_LIBRARY = {
    "SECTIONS": (
        ("Components", ["djangd/components"]),
        ("Example",    ["example_app"]),
    ),
    "PATTERN_BASE_TEMPLATE_NAME": "example_app/base.html",
    "BASE_TEMPLATE_NAMES": ["example_app/base.html"],
    "TEMPLATE_SUFFIX": ".html",
}
