import pytest
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
def test_swap_hints(hint, hints_swap_details_dto):
    # Arrange
    storage = HintStorageImplementation()

    # Act
    storage.swap_hints(
        hints_swap_details=hints_swap_details_dto
    )

    # Assert
    first_hint = Hint.objects.get(id=1)
    second_hint = Hint.objects.get(id=2)
    assert first_hint.hint_number == 2
    assert second_hint.hint_number == 1
