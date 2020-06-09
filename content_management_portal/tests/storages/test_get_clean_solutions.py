import pytest
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation


@pytest.mark.django_db
def test_get_clean_solutions(
        clean_solution, clean_solutions_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    response = storage.get_clean_solutions(question_id=question_id)

    # Assert
    clean_solution = response[0]
    expected_clean_solution = \
        clean_solutions_with_question_id_dtos[0]
    assert clean_solution.language == expected_clean_solution.language
    assert clean_solution.solution_content == \
        expected_clean_solution.solution_content
    assert clean_solution.file_name == expected_clean_solution.file_name
    assert clean_solution.question_id == question_id
    assert response == clean_solutions_with_question_id_dtos


@pytest.mark.django_db
def test_get_clean_solutions_when_no_clean_solutions(question):
    # Arrange
    question_id = 1
    storage = CleanSolutionStorageImplementation()
    expected_clean_solutions = []

    # Act
    clean_solutions = storage.get_clean_solutions(question_id=question_id)

    # Assert
    assert clean_solutions == expected_clean_solutions
