from django.apps import AppConfig


class FgAppConfig(AppConfig):
    name = "fg"

    def ready(self):
        from fg import signals # pylint: disable=unused-variable
