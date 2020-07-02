from content_management_portal_auth.storages.user_storage_implementation import \
    UserStorageImplementation
import pytest
from content_management_portal_auth.exceptions.exceptions import InvalidPassword

@pytest.mark.django_db
def test_is_valid_password_when_not_valid_raises_error(create_user_admin):
    # Arrange
    username = "user1"
    password = "124"
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        storage.validate_password(
            username=username, password=password
        )


@pytest.mark.django_db
def test_is_valid_password_when_valid(create_user_admin):
    # Arrange
    username = "user1"
    password = "123"
    expected_user_id = 1
    storage = UserStorageImplementation()

    # Act
    user_id = storage.validate_password(
        username=username, password=password
    )

    # Assert
    assert user_id == expected_user_id
