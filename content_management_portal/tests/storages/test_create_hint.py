import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
def test_create_hint_return_test_case_dto(
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
    assert hint.hint_number == expected_dto.hint_number
    assert hint.title == expected_dto.title
    assert hint.content == expected_dto.content
    assert hint.content_type == expected_dto.content_type
