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

