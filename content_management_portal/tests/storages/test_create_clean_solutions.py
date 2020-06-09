import pytest
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import CleanSolution


@pytest.mark.django_db
def test_create_clean_solution_creates_data(question, clean_solution_dtos):
    # Arrange
    question_id = 1
    storage = CleanSolutionStorageImplementation()

    # Act
    storage.create_clean_solutions(
        question_id=question_id,
        clean_solution_dtos=clean_solution_dtos
    )

    # Assert
    clean_solution_1 = CleanSolution.objects.get(id=1)
    assert clean_solution_1.language == clean_solution_dtos[0].language
    assert clean_solution_1.solution_content == \
        clean_solution_dtos[0].solution_content
    assert clean_solution_1.file_name == clean_solution_dtos[0].file_name
    assert clean_solution_1.question_id == question_id
    clean_solution_2 = CleanSolution.objects.get(id=2)
    assert clean_solution_2.language == clean_solution_dtos[1].language
    assert clean_solution_2.solution_content == \
        clean_solution_dtos[1].solution_content
    assert clean_solution_2.file_name == clean_solution_dtos[1].file_name
    assert clean_solution_2.question_id == question_id


@pytest.mark.django_db
def test_create_clean_solution_when_empty_list_given_no_data_created(question):
    # Arrange
    question_id = 1
    clean_solution_dtos = []
    storage = CleanSolutionStorageImplementation()

    # Act
    storage.create_clean_solutions(
        question_id=question_id,
        clean_solution_dtos=clean_solution_dtos
    )

    # Assert
    assert CleanSolution.objects.all().count() == 0
