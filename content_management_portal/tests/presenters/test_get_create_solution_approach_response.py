import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.storages.dtos import \
    SolutionApproachDto




def test_get_create_solution_approach_response_when_solution_approach_given_returns_of_solution_approach(
        solution_approach_with_question_id_dict, solution_approach_dto
    ):
    # Arrange
    question_id = 1
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_solution_approach_response(
        solution_approach_dto=solution_approach_dto, question_id=question_id
    )

    # Assert
    assert response == solution_approach_with_question_id_dict
