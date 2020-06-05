from content_management_portal.storages.rough_solution_storage_implementation import\
    RoughSolutionStorageImplementation
from content_management_portal.models import RoughSolution
import pytest


@pytest.mark.django_db
def test_delete_rough_solution(rough_solution):
    # Arrange
    rough_solution_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    rough_solution = storage.delete_rough_solution(
        rough_solution_id=rough_solution_id
    )

    # Assert
    assert RoughSolution.objects.filter(id=rough_solution_id).exists() == False
