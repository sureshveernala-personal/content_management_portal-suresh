import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionsWithQuestionIdDto

@pytest.mark.django_db
def test_get_rough_solutions(
        rough_solution, rough_solutions_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    response = storage.get_rough_solutions(question_id=question_id)

    # Assert
    assert response == rough_solutions_with_question_id_dtos[0]
    rough_solution = response.rough_solutions[0]
    expected_rough_solution = \
        rough_solutions_with_question_id_dtos[0].rough_solutions[0]
    assert rough_solution.language == expected_rough_solution.language
    assert rough_solution.solution_content == \
        expected_rough_solution.solution_content
    assert rough_solution.file_name == expected_rough_solution.file_name
    assert response.question_id == question_id


@pytest.mark.django_db
def test_get_rough_solutions_when_no_rough_solutions(question):
    # Arrange
    question_id = 1
    storage = RoughSolutionStorageImplementation()
    expected_rough_solutions = RoughSolutionsWithQuestionIdDto(
        question_id=1,rough_solutions=[]
    )

    # Act
    rough_solutions = storage.get_rough_solutions(question_id=question_id)

    # Assert
    assert rough_solutions == expected_rough_solutions
