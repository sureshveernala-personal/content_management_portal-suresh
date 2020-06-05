from content_management_portal.storages.prefilled_code_storage_implementation import\
    PrefilledCodeStorageImplementation
from content_management_portal.models import PrefilledCode
import pytest


@pytest.mark.django_db
def test_delete_prefilled_code(prefilled_code):
    # Arrange
    prefilled_code_id = 1
    storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_code = storage.delete_prefilled_code(
        prefilled_code_id=prefilled_code_id
    )

    # Assert
    assert PrefilledCode.objects.filter(id=prefilled_code_id).exists() == False
