import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation


@pytest.mark.django_db
def test_is_valid_rough_solution_id_when_valid_return_true(rough_solution):
    # Arrange
    rough_solution_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    is_valid = storage.is_valid_rough_solution_id(
        rough_solution_id=rough_solution_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_valid_rough_solution_id_when_invalid_return_false():
    # Arrange
    rough_solution_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    is_valid = storage.is_valid_rough_solution_id(
        rough_solution_id=rough_solution_id
    )

    # Assert
    assert is_valid == False
