SECRET_KEY = "test"
DEBUG = True
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth", "djangd_framework"]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    },
]
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
