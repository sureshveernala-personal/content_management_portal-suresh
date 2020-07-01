from typing import List
from content_management_portal_auth.storages.user_storage_implementation \
    import UserStorageImplementation
from content_management_portal_auth.interactors.get_users_details_interactor\
    import GetUsersDetailsInteractor


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids):
        user_storage = UserStorageImplementation()
        interactor = GetUsersDetailsInteractor(
            user_storage=user_storage, user_ids=user_ids
        )

        user_dtos = interactor.get_users_details()
        return user_dtos
