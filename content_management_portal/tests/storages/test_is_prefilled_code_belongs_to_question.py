import pytest
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation


@pytest.mark.django_db
def test_is_prefilled_code_belongs_to_question_when_valid_return_true(
        prefilled_code
    ):
    # Arrange
    prefilled_code_id = 1
    question_id = 1
    storage = PrefilledCodeStorageImplementation()

    # Act
    is_valid = storage.is_prefilled_code_belongs_to_question(
        prefilled_code_id=prefilled_code_id, question_id=question_id
    )

    # Assert
    assert is_valid == True

@pytest.mark.django_db
def test_is_prefilled_code_belongs_to_question_when_invalid_return_false(
        prefilled_code
    ):
    # Arrange
    prefilled_code_id = 1
    question_id = 2
    storage = PrefilledCodeStorageImplementation()

    # Act
    is_valid = storage.is_prefilled_code_belongs_to_question(
        prefilled_code_id=prefilled_code_id, question_id=question_id
    )

    # Assert
    assert is_valid == False
