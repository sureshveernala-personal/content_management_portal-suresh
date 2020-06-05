import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.models import Hint
from content_management_portal.interactors.storages.dtos import QuestionDto,\
    DescriptionDto


@pytest.mark.django_db
def test_create_hint_return_question_dto(
        question, hint_dto_without_hint_id,
        hint_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    expected_dto = hint_with_question_id_dto
    storage = HintStorageImplementation()

    # Act
    response_dto = storage.create_hint(
        question_id=question_id,
        hint_details=hint_dto_without_hint_id
    )

    # Assert
    assert response_dto == expected_dto
    assert Hint.objects.filter(id=1).exists()
    hint = Hint.objects.get(id=1)
    hint_dto = expected_dto.hint
    assert hint.hint_number == hint_dto.hint_number
    assert hint.title == hint_dto.title
    assert hint.content == hint_dto.description.content
    assert hint.content_type == hint_dto.description.content_type
