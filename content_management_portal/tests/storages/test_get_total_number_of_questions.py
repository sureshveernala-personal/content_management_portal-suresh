from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
import pytest


@pytest.mark.django_db
def get_total_number_of_questions_when_no_questions():
    # Arrange
    expected_total_questions_number = None
    storage = QuestionStorageImplementation()

    # Act
    total_number_of_questions = storage.get_total_number_of_questions()

    # Assert
    assert total_number_of_questions == expected_total_questions_number


@pytest.mark.django_db
def get_total_number_of_questions_when_having_questions(question):
    # Arrange
    expected_total_questions_number = 2
    storage = QuestionStorageImplementation()

    # Act
    total_number_of_questions = storage.get_total_number_of_questions()

    # Assert
    assert total_number_of_questions == expected_total_questions_number
