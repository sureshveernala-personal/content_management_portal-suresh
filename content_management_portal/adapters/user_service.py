from typing import List
from content_management_portal.interactors.storages.dtos import UserDto


class UserService:

    @property
    def interface(self):
        from content_management_portal_auth.interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()


    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)
        local_user_dtos = self._conver_into_local_user_dtos(
            user_dtos=user_dtos
        )
        return local_user_dtos

    @staticmethod
    def _conver_into_local_user_dtos(user_dtos: List[UserDto]):
        local_user_dtos = [
            UserDto(username=user_dto.username, user_id=user_dto.user_id)
            for user_dto in user_dtos
        ]
        return local_user_dtos
