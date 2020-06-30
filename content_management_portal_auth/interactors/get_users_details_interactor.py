from typing import List
from content_management_portal_auth.interactors.storages.\
    user_storage_interface import UserStorageInterface
from content_management_portal_auth.presenters.presenter_implementation \
    import PresenterInterface
from content_management_portal_auth.exceptions.exceptions import InvalidUserIds


class GetUsersDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface, user_ids: List[int]):
        self.user_storage = user_storage
        self.user_ids = user_ids


    def get_users_details_wrapper(self, presenter: PresenterInterface):
        try:
            user_dtos = self.get_users_details()
        except InvalidUserIds as error:
            presenter.raise_invalid_user_ids_exception(error=error)

        response = presenter.get_users_details_response(user_dtos=user_dtos)
        return response


    def get_users_details(self):
        self._validate_user_ids()
        user_dtos = self.user_storage.get_users_details(user_ids=self.user_ids)
        return user_dtos


    def _validate_user_ids(self):
        total_user_ids = self.user_storage.get_user_ids()
        invalid_user_ids = [
            user_id
            for user_id in self.user_ids
            if user_id not in total_user_ids
        ]
        if invalid_user_ids:
            raise InvalidUserIds(user_ids=invalid_user_ids)
