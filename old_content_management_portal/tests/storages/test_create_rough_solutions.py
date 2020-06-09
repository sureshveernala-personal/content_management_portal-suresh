import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation
from content_management_portal.dtos.dtos import RoughSolutionDto
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import RoughSolution


@pytest.mark.django_db
def test_create_rough_solution_creates_data(question, rough_solution_dtos):
    # Arrange
    question_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    storage.create_rough_solutions(
        question_id=question_id,
        rough_solutions_dtos=rough_solution_dtos
    )

    # Assert
    rough_solution_1 = RoughSolution.objects.get(id=1)
    assert rough_solution_1.language == rough_solution_dtos[0].language
    assert rough_solution_1.solution_content == \
        rough_solution_dtos[0].solution_content
    assert rough_solution_1.file_name == rough_solution_dtos[0].file_name
    assert rough_solution_1.question_id == question_id
    rough_solution_2 = RoughSolution.objects.get(id=2)
    assert rough_solution_2.language == rough_solution_dtos[1].language
    assert rough_solution_2.solution_content == \
        rough_solution_dtos[1].solution_content
    assert rough_solution_2.file_name == rough_solution_dtos[1].file_name
    assert rough_solution_2.question_id == question_id


@pytest.mark.django_db
def test_create_rough_solution_when_empty_list_given_no_data_created(question):
    # Arrange
    question_id = 1
    rough_solution_dtos = []
    storage = RoughSolutionStorageImplementation()

    # Act
    storage.create_rough_solutions(
        question_id=question_id,
        rough_solutions_dtos=rough_solution_dtos
    )

    # Assert
    assert RoughSolution.objects.all().count() == 0
