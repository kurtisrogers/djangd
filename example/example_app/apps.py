from django.apps import AppConfig


class ExampleAppConfig(AppConfig):
    name = "example_app"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        from . import components  # noqa: F401
