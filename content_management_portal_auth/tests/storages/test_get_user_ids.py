import pytest
from content_management_portal_auth.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
def test_get_user_ids(create_users):
    # Arrange
    user_ids = [1, 2, 3, 4]
    storage = UserStorageImplementation()

    # Act
    response_user_dtos = storage.get_user_ids()

    # Arrange
    assert response_user_dtos == user_ids


@pytest.mark.django_db
def test_get_user_ids_when_no_users_availble():
    # Arrange
    user_ids = []
    storage = UserStorageImplementation()

    # Act
    response_user_dtos = storage.get_user_ids()

    # Arrange
    assert response_user_dtos == user_ids
