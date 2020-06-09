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
