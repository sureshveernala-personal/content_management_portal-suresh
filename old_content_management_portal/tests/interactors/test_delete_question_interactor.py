from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.delete_problem_statement_interactor\
    import DeleteProblemStatementInteractor
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
import pytest


def test_delete_statement_interactor_with_invalid_question_id():
    # Arrange
    question_id = 1
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteProblemStatementInteractor(
        problem_statement_storage=problem_statement_storage,
        presenter=presenter
    )
    problem_statement_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_problem_statement(question_id=question_id)

    # Assert
    problem_statement_storage.delete_problem_statement.assert_not_called()


def test_delete_statement_interactor():
    # Arrange
    question_id = 1
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteProblemStatementInteractor(
        problem_statement_storage=problem_statement_storage,
        presenter=presenter
    )
    problem_statement_storage.delete_problem_statement.return_value = None

    # Act
    interactor.delete_problem_statement(question_id=question_id)

    # Assert
    problem_statement_storage.delete_problem_statement.assert_called_once_with(
        question_id=question_id
    )
