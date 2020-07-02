import pytest
from content_management_portal_auth.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
def test_get_user_details_return_list(create_users, create_user_dtos):
    # Arrange
    user_ids = [1, 2]
    storage = UserStorageImplementation()

    # Act
    response_user_dtos = storage.get_users_details(user_ids=user_ids)

    # Arrange
    assert response_user_dtos == create_user_dtos[:2]


@pytest.mark.django_db
def test_get_user_details_when_empty_list_passes_return_empty_list(create_users):
    # Arrange
    user_ids = []
    storage = UserStorageImplementation()

    # Act
    response_user_dtos = storage.get_users_details(user_ids=user_ids)

    # Arrange
    assert response_user_dtos == []
