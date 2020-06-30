import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal_auth.interactors.storages.\
    user_storage_interface import UserStorageInterface
from content_management_portal_auth.interactors.\
    get_users_details_interactor import GetUsersDetailsInteractor
from content_management_portal_auth.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal_auth.interactors.storages.dtos import\
    UserDto


def test_get_users_details_with_invalid_user_ids():
    # Arrange
    user_ids = [1, 2]
    user_storage = create_autospec(UserStorageInterface)
    interactor = GetUsersDetailsInteractor(
        user_storage=user_storage,user_ids=user_ids
    )
    presenter = create_autospec(PresenterInterface)
    user_storage.get_user_ids.return_value = [1]
    presenter.raise_invalid_user_ids_exception.side_effect = NotFound
    

    # Act
    with pytest.raises(NotFound):
        interactor.get_users_details_wrapper(presenter=presenter)

    # Assert
    kwargs = presenter.raise_invalid_user_ids_exception.call_args.kwargs
    error = kwargs['error']
    user_ids = error.user_ids
    assert user_ids == [2]


def test_get_user_details_with_valid_details():
    # Arrange
    user_ids = [1, 2]
    excepted_dicts = [
        {
            "username": "suresh",
            "user_id": 1
        }
    ]
    excepted_dtos = [
        UserDto(username="suresh", user_id=1)
    ]

    user_storage = create_autospec(UserStorageInterface)
    interactor = GetUsersDetailsInteractor(
        user_storage=user_storage,user_ids=user_ids
    )
    presenter = create_autospec(PresenterInterface)
    user_storage.get_user_ids.return_value = [1, 2]
    user_storage.get_users_details.return_value = excepted_dtos
    presenter.get_users_details_response.return_value = excepted_dicts


    # Act
    user_dicts = interactor.get_users_details_wrapper(presenter=presenter)

    # Assert
    user_storage.get_users_details.assert_called_once_with(user_ids=user_ids)
    presenter.get_users_details_response.assert_called_once_with(
        user_dtos=excepted_dtos
    )
    assert user_dicts == excepted_dicts
