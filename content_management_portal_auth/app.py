from django.apps import AppConfig


class ContentManagementPortalAuthAppConfig(AppConfig):
    name = "content_management_portal_auth"

    def ready(self):
        from content_management_portal_auth import signals # pylint: disable=unused-variable
