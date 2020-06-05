import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation


@pytest.mark.django_db
def test_get_given_question_test_case_ids_when_no_test_cases_return_empty_list():
    # Arrange
    expected_test_cases = []
    question_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    test_cases = storage.get_given_question_test_case_ids(
        question_id=question_id
    )

    # Assert
    assert test_cases == expected_test_cases

@pytest.mark.django_db
def test_get_given_question_test_case_ids_when_test_cases_availble_return_list(
        test_case
    ):
    # Arrange
    expected_test_cases = [1, 2, 3]
    question_id = 1
    storage = TestCaseStorageImplementation()

    # Act
    test_cases = storage.get_given_question_test_case_ids(
        question_id=question_id
    )

    # Assert
    assert test_cases == expected_test_cases
