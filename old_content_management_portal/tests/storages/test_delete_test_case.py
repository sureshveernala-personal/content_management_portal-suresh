from content_management_portal.storages.test_case_storage_implementation import\
    TestCaseStorageImplementation
from content_management_portal.models import TestCase
import pytest


@pytest.mark.django_db
def test_delete_test_case(test_case):
    # Arrange
    test_case_id = 1
    question_id =1
    storage = TestCaseStorageImplementation()

    # Act
    test_case = storage.delete_test_case(
        test_case_id=test_case_id, question_id=question_id
    )

    # Assert
    assert TestCase.objects.filter(id=test_case_id).exists() == False
    assert _check_all_test_case_numbers_are_decreased(question_id=question_id)

def _check_all_test_case_numbers_are_decreased(question_id: int):
    test_cases = TestCase.objects.filter(question_id=question_id)
    expected_test_case_number = 1
    for test_case in test_cases:
        assert test_case.test_case_number == expected_test_case_number
        expected_test_case_number += 1
    return True
