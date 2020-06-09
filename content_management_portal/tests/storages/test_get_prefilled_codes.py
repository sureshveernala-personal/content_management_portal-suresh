import pytest
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation


@pytest.mark.django_db
def test_get_prefilled_codes(
        prefilled_code, prefilled_codes_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    storage = PrefilledCodeStorageImplementation()

    # Act
    response = storage.get_prefilled_codes(question_id=question_id)

    # Assert
    expected_prefilled_code = \
        prefilled_codes_with_question_id_dtos[0]
    prefilled_code = response[0]
    assert prefilled_code.language == expected_prefilled_code.language
    assert prefilled_code.solution_content == \
        expected_prefilled_code.solution_content
    assert prefilled_code.file_name == expected_prefilled_code.file_name
    assert prefilled_code.question_id == question_id
    assert response == prefilled_codes_with_question_id_dtos



@pytest.mark.django_db
def test_get_prefilled_codes_when_no_prefilled_codes(question):
    # Arrange
    question_id = 1
    storage = PrefilledCodeStorageImplementation()
    expected_prefilled_codes = []

    # Act
    prefilled_codes = storage.get_prefilled_codes(question_id=question_id)

    # Assert
    assert prefilled_codes == expected_prefilled_codes
