import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionsWithQuestionIdDto


def test_get_create_rough_solutions_response_when_no_rough_solutions_returns_empty_list():
    # Arrange
    presenter = PresenterImplementation()
    rough_solution_dtos = RoughSolutionsWithQuestionIdDto(
        question_id=1,rough_solutions=[]
    )
    excepted_response = {
        "question_id":1,
        "rough_solutions": []
    }

    # Act
    response = presenter.get_create_rough_solutions_response(
        rough_solutions_dto_with_question_id\
        =rough_solution_dtos
    )

    # Assert
    assert response == excepted_response


def test_get_create_rough_solutions_response_when_rough_solutions_given_returns_list_of_rough_solutions(
        rough_solution_with_question_id_dicts, rough_solution_with_question_id_dtos
    ):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_rough_solutions_response(
        rough_solutions_dto_with_question_id=\
        rough_solution_with_question_id_dtos
    )

    # Assert
    assert response == rough_solution_with_question_id_dicts
