import pytest
import json
from content_management_portal.presenters.presenter_implementation import\
    CreateProblemStatementPresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound


def test_get_create_problem_statement_response(question_dto, question_dict):
    # Arrange
    presenter = CreateProblemStatementPresenterImplementation()

    # Act
    response = presenter.get_create_problem_statement_response(
        question_dto=question_dto
    )

    # Assert
    assert json.loads(response.content) == question_dict
