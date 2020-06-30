from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal_auth.interactors.storages.dtos import UserDto


class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: str):
        pass


    @abstractmethod
    def validate_password(self, username: str, password: str):
        pass


    @abstractmethod
    def get_user_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> UserDto:
        pass
