import pytest
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation
from content_management_portal.dtos.dtos import PrefilledCodeDto
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
def test_create_prefilled_code_creates_data(question, prefilled_code_dtos):
    # Arrange
    question_id = 1
    storage = PrefilledCodeStorageImplementation()

    # Act
    storage.create_prefilled_codes(
        question_id=question_id,
        prefilled_code_dtos=prefilled_code_dtos
    )

    # Assert
    prefilled_code_1 = PrefilledCode.objects.get(id=1)
    assert prefilled_code_1.language == prefilled_code_dtos[0].language
    assert prefilled_code_1.solution_content == \
        prefilled_code_dtos[0].solution_content
    assert prefilled_code_1.file_name == prefilled_code_dtos[0].file_name
    assert prefilled_code_1.question_id == question_id
    prefilled_code_2 = PrefilledCode.objects.get(id=2)
    assert prefilled_code_2.language == prefilled_code_dtos[1].language
    assert prefilled_code_2.solution_content == \
        prefilled_code_dtos[1].solution_content
    assert prefilled_code_2.file_name == prefilled_code_dtos[1].file_name
    assert prefilled_code_2.question_id == question_id


@pytest.mark.django_db
def test_create_prefilled_code_when_empty_list_given_no_data_created(question):
    # Arrange
    question_id = 1
    prefilled_code_dtos = []
    storage = PrefilledCodeStorageImplementation()

    # Act
    storage.create_prefilled_codes(
        question_id=question_id,
        prefilled_code_dtos=prefilled_code_dtos
    )

    # Assert
    assert PrefilledCode.objects.all().count() == 0
