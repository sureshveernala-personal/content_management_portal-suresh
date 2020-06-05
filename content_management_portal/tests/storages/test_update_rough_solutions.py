import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import RoughSolution


@pytest.mark.django_db
def test_update_rough_solutions_update_rough_solution(
        rough_solution, updated_rough_solution_dtos
    ):
    # Arrange
    question_id = 1
    rough_solution_ids = [1]
    rough_solution_with_question_id_dto = \
        updated_rough_solution_dtos[0]
    storage = RoughSolutionStorageImplementation()

    # Act
    storage.update_rough_solutions(
        rough_solution_ids=rough_solution_ids,
        rough_solution_dtos=updated_rough_solution_dtos
    )

    # Assert
    rough_solution = RoughSolution.objects.get(id=1)
    assert rough_solution.language == \
        rough_solution_with_question_id_dto.language
    assert rough_solution.solution_content == \
        rough_solution_with_question_id_dto.solution_content
    assert rough_solution.file_name == \
        rough_solution_with_question_id_dto.file_name
    assert rough_solution.question_id == question_id
