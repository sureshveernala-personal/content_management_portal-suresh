from content_management_portal_auth.interactors.storages.\
    user_storage_interface import UserStorageInterface
from content_management_portal_auth.models import User
from content_management_portal_auth.exceptions.exceptions import InvalidPassword
from typing import List
from content_management_portal_auth.interactors.storages.dtos import UserDto


class UserStorageImplementation(UserStorageInterface):

    def is_valid_username(self, username: str):
        is_valid_username = User.objects.filter(username=username).exists()
        return is_valid_username


    def validate_password(self, username: str, password: str):
        user = User.objects.get(username=username)
        if user.check_password(password):
            return user.id
        else:
            raise InvalidPassword


    def get_user_ids(self):
        user_ids = User.objects.values_list('id', flat=True)
        return list(user_ids)



    def get_users_details(self, user_ids: List[int]):
        users = User.objects.filter(id__in=user_ids)
        user_dtos = self._get_user_dtos(users=users)
        return user_dtos


    def _get_user_dtos(self, users: List[User]):
        user_dtos = [
            self._get_user_dto(user=user)
            for user in users
        ]
        return user_dtos


    @staticmethod
    def _get_user_dto(user: User):
        user_dto = UserDto(
            username=user.username,
            user_id=user.id
        )
        return user_dto
