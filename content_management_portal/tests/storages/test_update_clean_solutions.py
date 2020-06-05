import pytest
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import CleanSolution


@pytest.mark.django_db
def test_update_clean_solutions_update_clean_solution(
        clean_solution, updated_clean_solution_dtos
    ):
    # Arrange
    question_id = 1
    clean_solution_ids = [1]
    clean_solution_with_question_id_dto = \
        updated_clean_solution_dtos[0]
    storage = CleanSolutionStorageImplementation()

    # Act
    storage.update_clean_solutions(
        clean_solution_ids=clean_solution_ids,
        clean_solution_dtos=updated_clean_solution_dtos
    )

    # Assert
    clean_solution = CleanSolution.objects.get(id=1)
    assert clean_solution.language == \
        clean_solution_with_question_id_dto.language
    assert clean_solution.solution_content == \
        clean_solution_with_question_id_dto.solution_content
    assert clean_solution.file_name == \
        clean_solution_with_question_id_dto.file_name
    assert clean_solution.question_id == question_id
