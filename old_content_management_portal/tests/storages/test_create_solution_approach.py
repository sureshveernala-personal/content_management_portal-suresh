import pytest
from content_management_portal.storages.solution_approach_storage_implementation \
    import SolutionApproachStorageImplementation
from content_management_portal.interactors.storages.dtos import \
     SolutionApproachDto
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import SolutionApproach


@pytest.mark.django_db
def test_create_solution_approach_creates_data(question, solution_approach_dto):
    # Arrange
    question_id = 1
    storage = SolutionApproachStorageImplementation()

    # Act
    storage.create_solution_approach(
        question_id=question_id,
        solution_approach_details=solution_approach_dto
    )

    # Assert
    solution_approach = SolutionApproach.objects.get(id=1)
    assert solution_approach.title == solution_approach_dto.title
    assert solution_approach.description_content == \
        solution_approach_dto.description_content
    assert solution_approach.description_content_type == \
        solution_approach_dto.description_content_type
    assert solution_approach.complexity_analysis_content == \
        solution_approach_dto.complexity_analysis_content
    assert solution_approach.complexity_analysis_content_type == \
        solution_approach_dto.complexity_analysis_content_type
    assert solution_approach.question_id == question_id
