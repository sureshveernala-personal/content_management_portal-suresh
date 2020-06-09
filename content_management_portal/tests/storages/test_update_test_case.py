import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase
from content_management_portal.interactors.storages.dtos import QuestionDto,\
    DescriptionDto


@pytest.mark.django_db
def test_update_test_case_return_test_case_dto(
        test_case, updated_test_case_dto, updted_test_case_with_question_id_dto
    ):
    # Arrange
    expected_dto = updted_test_case_with_question_id_dto
    storage = TestCaseStorageImplementation()

    # Act
    response_dto = storage.update_test_case(
        test_case_details=updated_test_case_dto
    )

    # Assert
    assert response_dto == expected_dto
    assert TestCase.objects.filter(id=1).exists()
    test_case = TestCase.objects.get(id=1)
    assert test_case.test_case_number == expected_dto.test_case_number
    assert test_case.input == expected_dto.input
    assert test_case.output == expected_dto.output
    assert test_case.is_hidden == expected_dto.is_hidden
