from content_management_portal_auth.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal_auth.interactors.storages.dtos import UserDto


def test_get_users_details_response():
    # Arrange
    user_dtos = [
        UserDto(username="suresh", user_id=1)
    ]
    expected_user_dicts = [
        {
            "user_id": 1,
            "username": "suresh"
        }
    ]
    presenter = PresenterImplementation()

    # Act
    user_dicts = presenter.get_users_details_response(user_dtos=user_dtos)

    # Assert
    assert user_dicts == expected_user_dicts
