from content_management_portal.interactors.storages.user_storage_interface \
    import UserStorageInterface
from content_management_portal.models import User
from content_management_portal.exceptions.exceptions import InvalidPassword


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
