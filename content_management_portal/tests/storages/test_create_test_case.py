import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
def test_create_test_case_return_question_dto(
        question, test_case_dto_without_test_case_id,
        test_case_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    expected_dto = test_case_with_question_id_dto
    storage = TestCaseStorageImplementation()

    # Act
    response_dto = storage.create_test_case(
        question_id=question_id,
        test_case_details=test_case_dto_without_test_case_id
    )

    # Assert
    assert TestCase.objects.filter(id=1).exists()
    test_case = TestCase.objects.get(id=1)
    assert test_case.test_case_number == expected_dto.test_case_number
    assert test_case.input == expected_dto.input
    assert test_case.output == expected_dto.output
    assert test_case.is_hidden == expected_dto.is_hidden
    assert response_dto == expected_dto
