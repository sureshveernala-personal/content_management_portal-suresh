import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation


@pytest.mark.django_db
def test_is_hint_belongs_to_question_when_valid_return_true(hint):
    # Arrange
    hint_id = 1
    question_id = 1
    storage = HintStorageImplementation()

    # Act
    is_valid = storage.is_hint_belongs_to_question(
        question_id=question_id, hint_id=hint_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_hint_belongs_to_question_when_invalid_return_false(question):
    # Arrange
    hint_id = 1
    question_id = 1
    storage = HintStorageImplementation()

    # Act
    is_valid = storage.is_hint_belongs_to_question(
        question_id=question_id, hint_id=hint_id
    )

    # Assert
    assert is_valid == False
