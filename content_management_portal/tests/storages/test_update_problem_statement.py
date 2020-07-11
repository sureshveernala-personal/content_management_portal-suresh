from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.models import Question
# from content_management_portal.dtos.dtos import DescriptionDto
from content_management_portal.constants.enums import DescriptionType
import pytest
from content_management_portal.interactors.storages.dtos import  StatementDto,\
    QuestionDto, DescriptionDto

@pytest.mark.django_db
def test_update_problem_stament_return_question_dto(
        question, updated_question_dto, updated_description_dto
    ):
    # Arrange
    user_id = 1
    question_id = 1
    short_text = "new_short_text1"
    storage = QuestionStorageImplementation()

    # Act
    response = storage.update_problem_statement(
        user_id=user_id, question_dto=updated_question_dto
    )

    # Assert
    assert response == updated_question_dto
    assert Question.objects.filter(id=question_id).exists()
    question = Question.objects.get(id=question_id)
    assert question.created_by_id == user_id
    assert question.short_text == short_text
    assert question.content == updated_question_dto.content
    assert question.content_type == updated_question_dto.content_type
