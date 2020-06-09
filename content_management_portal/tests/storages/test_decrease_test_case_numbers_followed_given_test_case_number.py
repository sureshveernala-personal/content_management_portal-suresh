from content_management_portal.storages.test_case_storage_implementation import\
    TestCaseStorageImplementation
from content_management_portal.models import TestCase
import pytest


@pytest.mark.django_db
def test_decrease_test_case_numbers_followed_given_test_case_number():
    # Arrange
    question_id = 1
    test_case_number = 1
    storage = TestCaseStorageImplementation()

    # Act
    storage.decrease_test_case_numbers_followed_given_test_case_number(
        question_id=question_id, test_case_number=test_case_number
    )

    # Assert
    test_cases = TestCase.objects.filter(test_case_number__gt=test_case_number)
    expected_test_case_number = 1
    for test_case in test_cases:
        assert test_case.test_case_number == expected_test_case_number
        expected_test_case_number += 1
    return True
