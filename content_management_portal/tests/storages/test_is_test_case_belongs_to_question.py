import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation


@pytest.mark.django_db
def test_is_test_case_belongs_to_question_when_valid_return_true(test_case):
    # Arrange
    test_case_id = 1
    question_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    is_valid = storage.is_test_case_belongs_to_question(
        question_id=question_id, test_case_id=test_case_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_test_case_belongs_to_question_when_invalid_return_false(question):
    # Arrange
    test_case_id = 1
    question_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    is_valid = storage.is_test_case_belongs_to_question(
        question_id=question_id, test_case_id=test_case_id
    )

    # Assert
    assert is_valid == False
