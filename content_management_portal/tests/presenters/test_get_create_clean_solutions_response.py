import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


def test_get_create_clean_solutions_response_when_no_clean_solutions_returns_empty_list():
    # Arrange
    presenter = PresenterImplementation()
    clean_solution_dtos = []
    excepted_response = {
        "question_id":1,
        "clean_solutions": []
    }

    # Act
    response = presenter.get_create_clean_solutions_response(
        question_id=1,
        clean_solution_with_question_id_dtos=clean_solution_dtos
    )

    # Assert
    assert response == excepted_response


def test_get_create_clean_solutions_response_when_clean_solutions_given_returns_list_of_clean_solutions(
        clean_solution_with_question_id_dicts,
        clean_solution_with_question_id_dtos
    ):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_clean_solutions_response(
        question_id=1,
        clean_solution_with_question_id_dtos=\
        clean_solution_with_question_id_dtos
    )

    # Assert
    assert response == clean_solution_with_question_id_dicts
