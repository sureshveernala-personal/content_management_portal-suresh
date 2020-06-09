import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound


def test_get_create_problem_statement_response(question_dto, question_dict):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_problem_statement_response(
        question_dto=question_dto
    )

    # Assert
    assert response == question_dict
