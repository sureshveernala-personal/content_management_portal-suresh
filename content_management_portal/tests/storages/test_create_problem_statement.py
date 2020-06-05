from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.models import Question
# from content_management_portal.dtos.dtos import DescriptionDto
from content_management_portal.constants.enums import DescriptionType
import pytest
from content_management_portal.interactors.storages.dtos import QuestionDto,\
    DescriptionDto


@pytest.mark.django_db
def test_create_problem_statement_return_question_dto(
        user, question_dto, description_dto
    ):
    # Arrange
    user_id = 1
    short_text = "short_text1"
    storage = QuestionStorageImplementation()

    # Act
    response_dto = storage.create_problem_statement(
        user_id=user_id,
        short_text=short_text,
        description=description_dto
    )

    # Assert
    assert response_dto == question_dto
    assert Question.objects.filter(id=1).exists()
    question = Question.objects.get(id=1)
    assert question.created_by_id == user_id
    assert question.short_text == question_dto.short_text
    assert question.content == description_dto.content
    assert question.content_type == description_dto.content_type
