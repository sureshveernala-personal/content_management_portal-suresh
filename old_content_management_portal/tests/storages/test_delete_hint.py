from content_management_portal.storages.hint_storage_implementation import\
    HintStorageImplementation
from content_management_portal.models import Hint
import pytest


@pytest.mark.django_db
def test_delete_hint(hint):
    # Arrange
    hint_id = 1
    question_id =1
    storage = HintStorageImplementation()

    # Act
    hint = storage.delete_hint(
        hint_id=hint_id, question_id=question_id
    )

    # Assert
    assert Hint.objects.filter(id=hint_id).exists() == False
    assert _check_all_hint_numbers_are_decreased(question_id=question_id)

def _check_all_hint_numbers_are_decreased(question_id: int):
    hints = Hint.objects.filter(question_id=question_id)
    expected_hint_number = 1
    for hint in hints:
        assert hint.hint_number == expected_hint_number
        expected_hint_number += 1
    return True
