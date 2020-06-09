import pytest
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation


@pytest.mark.django_db
def test_get_clean_solution_ids_when_no_clean_solutions_return_empty_list():
    # Arrange
    expected_rough_solutios = []
    question_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    clean_solutions = storage.get_question_clean_solution_ids(
        question_id=question_id
    )

    # Assert
    assert clean_solutions == expected_rough_solutios

@pytest.mark.django_db
def test_get_clean_solution_ids_when_clean_solutions_availble_return_list(
        clean_solution
    ):
    # Arrange
    expected_rough_solutios = [1]
    question_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    clean_solutions = storage.get_question_clean_solution_ids(
        question_id=question_id
    )

    # Assert
    assert clean_solutions == expected_rough_solutios
