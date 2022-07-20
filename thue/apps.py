from django.apps import AppConfig


class ThueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "thue"

    def ready(self):
        import thue.signals
