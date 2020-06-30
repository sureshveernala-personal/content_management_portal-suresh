from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal_auth.exceptions.exceptions import InvalidUserIds
from content_management_portal_auth.interactors.storages.dtos import UserDto


class PresenterInterface(ABC):
    @abstractmethod
    def raise_invalid_username_exception(self):
        pass


    @abstractmethod
    def raise_invalid_password_exception(self):
        pass


    @abstractmethod
    def login_response(self, access_token):
        pass


    @abstractmethod
    def raise_invalid_user_ids_exception(self, error: InvalidUserIds):
        pass


    @abstractmethod
    def get_users_details_response(self, user_dtos: List[UserDto]):
        pass
