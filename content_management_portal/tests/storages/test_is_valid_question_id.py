from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
import pytest


@pytest.mark.django_db
def test_is_valid_question_id_with_invalid_question_id_return_false():
    # Arrange
    invalid_question_id = 1
    storage = QuestionStorageImplementation()

    # Act
    is_valid_question_id = storage.is_valid_question_id(
        question_id=invalid_question_id
    )

    # Assert
    assert is_valid_question_id == False


@pytest.mark.django_db
def test_is_valid_question_with_valid_question_id_return_true(question):
    # Arrange
    valid_question_id = 1
    storage = QuestionStorageImplementation()

    # Act
    is_valid_question_id = storage.is_valid_question_id(
        question_id=valid_question_id
    )

    # Assert
    assert is_valid_question_id == True
