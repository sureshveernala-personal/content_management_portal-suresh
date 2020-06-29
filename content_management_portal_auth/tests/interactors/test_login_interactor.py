from unittest.mock import create_autospec, patch
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal_auth.interactors.storages.\
    user_storage_interface import UserStorageInterface
from content_management_portal_auth.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal_auth.interactors.login_interactor\
    import LoginInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import\
    OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
import datetime
from content_management_portal_auth.exceptions.exceptions import InvalidPassword


@pytest.mark.django_db
def test_login_interactor_with_invalid_username_raises_error():
    # Arrange
    username = "suresh"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage()
    user_storage.is_valid_username.return_value = False
    presenter.raise_invalid_username_exception.side_effect = NotFound
    interactor = LoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    # Act
    with pytest.raises(NotFound):
        interactor.login(username=username, password=password)

    # Assert
    user_storage.is_valid_username.assert_called_once_with(username=username)
    presenter.raise_invalid_username_exception.assert_called_once()


@pytest.mark.django_db
def test_login_interactor_with_invalid_password_raises_error():
    # Arrange
    username = "suresh"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage()
    user_storage.is_valid_username.return_value = True
    user_storage.validate_password.side_effect = InvalidPassword
    presenter.raise_invalid_password_exception.side_effect = Forbidden
    interactor = LoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    # Act
    with pytest.raises(Forbidden):
        interactor.login(username=username, password=password)

    # Assert
    user_storage.is_valid_username.assert_called_once_with(username=username)
    user_storage.validate_password.assert_called_once_with(
        username=username,
        password=password
    )
    presenter.raise_invalid_password_exception.assert_called_once()


access_token_dto = UserAuthTokensDTO(
    user_id=1,
    access_token='PbWOleEjL99tOoUPfPY3NR2rA9mphk',
    refresh_token='sFajX39Y1Ye9AjKUd2zKn3Yf4syryD',
    expires_in=datetime.datetime(2337, 4, 20, 2, 14, 3, 493790)
)


@pytest.mark.django_db
@patch.object(
    OAuthUserAuthTokensService,
    "create_user_auth_tokens",
    return_value=access_token_dto
)
def test_login_interactor_with_valid_details(token_service):
    # Arrange
    user_id = 1
    username = "user1"
    password = "123"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage()
    user_storage.is_valid_username.return_value = True
    user_storage.validate_password.return_value = user_id
    interactor = LoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    expected_access_token = {
        "user_id": 1,
        "access_token": 'PbWOleEjL99tOoUPfPY3NR2rA9mphk',
        "refresh_token": 'sFajX39Y1Ye9AjKUd2zKn3Yf4syryD',
        "expires_in": "2337-4-20 2:14:3.493790"
    }
    presenter.login_response.return_value = expected_access_token

    # Act
    response = interactor.login(username=username, password=password)

    # Assert
    user_storage.is_valid_username.assert_called_once_with(username=username)
    user_storage.validate_password.assert_called_once_with(
        username=username,
        password=password
    )
    presenter.login_response.assert_called_once_with(
        access_token=access_token_dto
    )
    assert response == expected_access_token
