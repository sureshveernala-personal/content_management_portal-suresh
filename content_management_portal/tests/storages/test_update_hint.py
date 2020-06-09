import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.models import Hint
from content_management_portal.interactors.storages.dtos import QuestionDto,\
    DescriptionDto


@pytest.mark.django_db
def test_update_hint_return_question_dto(
        hint, updated_hint_dto, updted_hint_with_question_id_dto
    ):
    # Arrange
    expected_dto = updted_hint_with_question_id_dto
    storage = HintStorageImplementation()

    # Act
    response_dto = storage.update_hint(
        hint_details=updated_hint_dto
    )

    # Assert
    assert response_dto == expected_dto
    assert Hint.objects.filter(id=1).exists()
    hint = Hint.objects.get(id=1)
    assert hint.hint_number == expected_dto.hint_number
    assert hint.content == expected_dto.content
    assert hint.content_type == expected_dto.content_type
    assert hint.title == expected_dto.title
