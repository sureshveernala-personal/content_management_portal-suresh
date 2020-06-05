import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation


@pytest.mark.django_db
def test_is_valid_hint_id_when_valid_return_true(hint):
    # Arrange
    hint_id = 1
    storage = HintStorageImplementation()

    # Act
    is_valid = storage.is_valid_hint_id(
        hint_id=hint_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_valid_hint_id_when_invalid_return_false():
    # Arrange
    hint_id = 1
    storage = HintStorageImplementation()

    # Act
    is_valid = storage.is_valid_hint_id(
        hint_id=hint_id
    )

    # Assert
    assert is_valid == False
