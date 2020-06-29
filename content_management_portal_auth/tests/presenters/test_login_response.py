from content_management_portal_auth.presenters.presenter_implementation import\
    PresenterImplementation
from common.dtos import UserAuthTokensDTO
import datetime

def test_raise_invalid_username_exception_raises_error():
    # Arrange
    access_token = UserAuthTokensDTO(
        user_id=1,
        access_token='djdfngGGnY5ZPx3SiZQdfGuKsIWyQI',
        refresh_token='4nv8uatHc9PL5GMoFfKFWyClKA1Ssn',
        expires_in=datetime.datetime(2337, 4, 18, 15, 27, 26, 374882)
    )
    expected_access_token_dict = {
        "user_id": 1,
        "access_token": 'djdfngGGnY5ZPx3SiZQdfGuKsIWyQI',
        "refresh_token": '4nv8uatHc9PL5GMoFfKFWyClKA1Ssn',
        "expires_in": '2337-04-18 15:27:26.374882'
    }
    presenter = PresenterImplementation()

    # Act
    access_token_dict = presenter.login_response(access_token=access_token)

    # Assert

    assert access_token_dict == expected_access_token_dict
