import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation


@pytest.mark.django_db
def test_get_hint_ids_when_no_hints_return_empty_list():
    # Arrange
    expected_hints = []
    storage = HintStorageImplementation()

    # Act
    hints = storage.get_hint_ids()

    # Assert
    assert hints == expected_hints

@pytest.mark.django_db
def test_get_hint_ids_when_hints_availble_return_list(hint):
    # Arrange
    expected_hints = [1, 2, 3]
    storage = HintStorageImplementation()

    # Act
    hints = storage.get_hint_ids()

    # Assert
    assert hints == expected_hints
