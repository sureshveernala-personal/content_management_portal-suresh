from content_management_portal.storages.hint_storage_implementation import\
    HintStorageImplementation
from content_management_portal.models import Hint
import pytest


@pytest.mark.django_db
def test_decrease_hint_numbers_followed_given_hint_number():
    # Arrange
    question_id = 1
    hint_number = 1
    storage = HintStorageImplementation()

    # Act
    storage.decrease_hint_numbers_followed_given_hint_number(
        question_id=question_id, hint_number=hint_number
    )

    # Assert
    hints = Hint.objects.filter(hint_number__gt=hint_number)
    expected_hint_number = 1
    for hint in hints:
        assert hint.hint_number == expected_hint_number
        expected_hint_number += 1
    return True
