import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation


@pytest.mark.django_db
def test_is_valid_test_case_id_when_valid_return_true(test_case):
    # Arrange
    test_case_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    is_valid = storage.is_valid_test_case_id(
        test_case_id=test_case_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_valid_test_case_id_when_invalid_return_false():
    # Arrange
    test_case_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    is_valid = storage.is_valid_test_case_id(
        test_case_id=test_case_id
    )

    # Assert
    assert is_valid == False
