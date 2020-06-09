import pytest
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
def test_update_prefilled_codes_update_prefilled_code(
        prefilled_code, updated_prefilled_code_dtos
    ):
    # Arrange
    question_id = 1
    prefilled_code_ids = [1]
    prefilled_code_with_question_id_dto = \
        updated_prefilled_code_dtos[0]
    storage = PrefilledCodeStorageImplementation()

    # Act
    storage.update_prefilled_codes(
        prefilled_code_ids=prefilled_code_ids,
        prefilled_code_dtos=updated_prefilled_code_dtos
    )

    # Assert
    prefilled_code = PrefilledCode.objects.get(id=1)
    assert prefilled_code.language == \
        prefilled_code_with_question_id_dto.language
    assert prefilled_code.solution_content == \
        prefilled_code_with_question_id_dto.solution_content
    assert prefilled_code.file_name == \
        prefilled_code_with_question_id_dto.file_name
    assert prefilled_code.question_id == question_id
