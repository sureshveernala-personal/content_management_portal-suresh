import pytest
from content_management_portal.storages.solution_approach_storage_implementation \
    import SolutionApproachStorageImplementation
from content_management_portal.models import SolutionApproach
from content_management_portal.interactors.storages.dtos import QuestionDto,\
    DescriptionDto


@pytest.mark.django_db
def test_update_solution_approach_return_question_dto(
        solution_approach, updated_solution_approach_dto
    ):
    # Arrange
    expected_dto = updated_solution_approach_dto
    storage = SolutionApproachStorageImplementation()

    # Act
    response_dto = storage.update_solution_approach(
        solution_approach_details=updated_solution_approach_dto
    )

    # Assert
    assert response_dto == expected_dto
    assert SolutionApproach.objects.filter(id=1).exists()
    solution_approach = SolutionApproach.objects.get(id=1)
    assert solution_approach.title == expected_dto.title
    assert solution_approach.description_content == \
        expected_dto.description_content
    assert solution_approach.description_content_type == \
        expected_dto.description_content_type
    assert solution_approach.complexity_analysis_content == \
        expected_dto.complexity_analysis_content
    assert solution_approach.complexity_analysis_content_type == \
        expected_dto.complexity_analysis_content_type
