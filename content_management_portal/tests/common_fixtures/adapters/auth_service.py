from typing import List

from content_management_portal.interactors.storages.dtos import UserDto


def prepare_get_user_dtos_mock(mocker, user_ids: List[int]):
    mock = mocker.patch(
        'content_management_portal.adapters.user_service.UserService.get_user_dtos'
    )
    user_dtos = [
        UserDto(
            user_id=user_id,
            username="user_{}".format(_index + 1),
        ) for _index, user_id in enumerate(user_ids)
    ]
    mock.return_value = user_dtos
    return mock
