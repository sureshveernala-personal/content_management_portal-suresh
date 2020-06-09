from content_management_portal.storages.test_case_storage_implementation import\
    TestCaseStorageImplementation
from content_management_portal.models import TestCase
import pytest


@pytest.mark.django_db
def test_get_max_test_case_number_when_no_test_cases():
    # Arrange
    question_id = 1
    storage = TestCaseStorageImplementation()
    expected_max_test_case_number = None

    # Act
    max_test_case_number = storage.get_max_test_case_number(question_id=question_id)

    # Assert
    assert expected_max_test_case_number == max_test_case_number


@pytest.mark.django_db
def test_get_max_test_case_number_when_having_test_cases_returns_count(test_case):
    # Arrange
    question_id = 1
    storage = TestCaseStorageImplementation()
    expected_max_test_case_number = 3

    # Act
    max_test_case_number = storage.get_max_test_case_number(question_id=question_id)

    # Assert
    assert expected_max_test_case_number == max_test_case_number
