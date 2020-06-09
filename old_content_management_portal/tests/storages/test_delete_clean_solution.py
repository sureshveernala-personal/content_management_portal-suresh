from content_management_portal.storages.clean_solution_storage_implementation import\
    CleanSolutionStorageImplementation
from content_management_portal.models import PrefilledCode
import pytest


@pytest.mark.django_db
def test_delete_clean_solution(clean_solution):
    # Arrange
    clean_solution_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    clean_solution = storage.delete_clean_solution(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert PrefilledCode.objects.filter(id=clean_solution_id).exists() == False
