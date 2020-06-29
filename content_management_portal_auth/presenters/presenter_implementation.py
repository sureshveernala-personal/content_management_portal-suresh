from datetime import datetime
from typing import List, Dict
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal_auth.interactors.presenters.presenter_interface\
    import PresenterInterface

from content_management_portal_auth.constants.exception_messages import\
    INVALID_USER_NAME, INVALID_PASSWORD

class PresenterImplementation(PresenterInterface):

    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USER_NAME)


    def raise_invalid_password_exception(self):
        raise Forbidden(*INVALID_PASSWORD)


    def login_response(self, access_token):
        access_token_dict = {
            "user_id": access_token.user_id,
            "access_token": access_token.access_token,
            "refresh_token": access_token.refresh_token,
            "expires_in": datetime.strftime(
                access_token.expires_in, "%Y-%m-%d %H:%M:%S.%f"
            )
        }
        return access_token_dict
