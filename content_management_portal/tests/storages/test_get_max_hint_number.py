from content_management_portal.storages.hint_storage_implementation import\
    HintStorageImplementation
from content_management_portal.models import Hint
import pytest


@pytest.mark.django_db
def test_get_max_hint_number_when_no_hints():
    # Arrange
    question_id = 1
    storage = HintStorageImplementation()
    expected_max_hint_number = None

    # Act
    max_hint_number = storage.get_max_hint_number(question_id=question_id)

    # Assert
    assert expected_max_hint_number == max_hint_number


@pytest.mark.django_db
def test_get_max_hint_number_when_having_hints_returns_count(hint):
    # Arrange
    question_id = 1
    storage = HintStorageImplementation()
    expected_max_hint_number = 3

    # Act
    max_hint_number = storage.get_max_hint_number(question_id=question_id)

    # Assert
    assert expected_max_hint_number == max_hint_number
