import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation


@pytest.mark.django_db
def test_get_given_question_hint_ids_when_no_hints_return_empty_list():
    # Arrange
    expected_hints = []
    question_id = 1
    storage = HintStorageImplementation()

    # Act
    hints = storage.get_given_question_hint_ids(
        question_id=question_id
    )

    # Assert
    assert hints == expected_hints

@pytest.mark.django_db
def test_get_given_question_hint_ids_when_hints_availble_return_list(
        hint
    ):
    # Arrange
    expected_hints = [1, 2, 3]
    question_id = 1
    storage = HintStorageImplementation()

    # Act
    hints = storage.get_given_question_hint_ids(
        question_id=question_id
    )

    # Assert
    assert hints == expected_hints
