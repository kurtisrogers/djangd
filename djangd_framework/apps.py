from django.apps import AppConfig


class DjangdFrameworkConfig(AppConfig):
    name = "djangd_framework"
    label = "djangd_framework"
    verbose_name = "djangd-framework"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        from . import components  # noqa: F401  (registers built-in components)
