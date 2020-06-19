from django.apps import AppConfig


class Covid19AppConfig(AppConfig):
    name = "covid_19"

    def ready(self):
        from covid_19 import signals # pylint: disable=unused-variable
