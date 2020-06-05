import pytest
from content_management_portal.storages.solution_approach_storage_implementation \
    import SolutionApproachStorageImplementation


@pytest.mark.django_db
def test_is_solution_approach_belongs_to_question_when_valid_return_true(solution_approach):
    # Arrange
    solution_approach_id = 1
    question_id = 1
    storage = SolutionApproachStorageImplementation()

    # Act
    is_valid = storage.is_solution_approach_belongs_to_question(
        question_id=question_id, solution_approach_id=solution_approach_id
    )

    # Assert
    assert is_valid == True


@pytest.mark.django_db
def test_is_solution_approach_belongs_to_question_when_invalid_return_false(question):
    # Arrange
    solution_approach_id = 1
    question_id = 1
    storage = SolutionApproachStorageImplementation()

    # Act
    is_valid = storage.is_solution_approach_belongs_to_question(
        question_id=question_id, solution_approach_id=solution_approach_id
    )

    # Assert
    assert is_valid == False
