import pytest
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation


@pytest.mark.django_db
def test_is_valid_clean_solution_id_when_valid_return_true(clean_solution):
    # Arrange
    clean_solution_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    is_valid = storage.is_valid_clean_solution_id(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_valid_clean_solution_id_when_invalid_return_false():
    # Arrange
    clean_solution_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    is_valid = storage.is_valid_clean_solution_id(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert is_valid == False
