import pytest
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation


@pytest.mark.django_db
def test_is_rough_solution_belongs_to_question_when_valid_return_true(rough_solution):
    # Arrange
    rough_solution_id = 1
    question_id = 1
    storage = RoughSolutionStorageImplementation()

    # Act
    is_valid = storage.is_rough_solution_belongs_to_question(
        rough_solution_id=rough_solution_id, question_id=question_id
    )

    # Assert
    assert is_valid == True

@pytest.mark.django_db
def test_is_rough_solution_belongs_to_question_when_invalid_return_false(rough_solution):
    # Arrange
    rough_solution_id = 1
    question_id = 2
    storage = RoughSolutionStorageImplementation()

    # Act
    is_valid = storage.is_rough_solution_belongs_to_question(
        rough_solution_id=rough_solution_id, question_id=question_id
    )

    # Assert
    assert is_valid == False
