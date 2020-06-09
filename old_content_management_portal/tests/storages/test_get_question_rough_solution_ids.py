import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation


@pytest.mark.django_db
def test_get_rough_solution_ids_when_no_rough_solutions_return_empty_list():
    # Arrange
    expected_rough_solutios = []
    question_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    rough_solutions = storage.get_question_rough_solution_ids(
        question_id=question_id
    )

    # Assert
    assert rough_solutions == expected_rough_solutios

@pytest.mark.django_db
def test_get_rough_solution_ids_when_rough_solutions_availble_return_list(rough_solution):
    # Arrange
    expected_rough_solutios = [1]
    question_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    rough_solutions = storage.get_question_rough_solution_ids(
        question_id=question_id
    )

    # Assert
    assert rough_solutions == expected_rough_solutios
