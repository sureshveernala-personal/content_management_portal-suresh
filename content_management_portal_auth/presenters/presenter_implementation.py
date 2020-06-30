from datetime import datetime
from typing import List, Dict
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal_auth.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal_auth.constants.exception_messages import\
    INVALID_USER_NAME, INVALID_PASSWORD, INVALID_USER_IDS
from content_management_portal_auth.exceptions.exceptions import InvalidUserIds
from content_management_portal_auth.interactors.storages.dtos import UserDto


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


    def raise_invalid_user_ids_exception(self, error: InvalidUserIds):
        raise NotFound(INVALID_USER_IDS)


    def get_users_details_response(self, user_dtos: List[UserDto]):
        user_dicts = self._get_user_dicts(user_dtos=user_dtos)
        return user_dicts


    def _get_user_dicts(self, user_dtos: List[UserDto]):
        user_dicts = [
            self._get_user_dict(user_dto=user_dto)
            for user_dto in user_dtos
        ]
        return user_dicts


    @staticmethod
    def _get_user_dict(user_dto: UserDto):
        user_dict = {
            "username": user_dto.username,
            "user_id": user_dto.user_id
        }
        return user_dict
