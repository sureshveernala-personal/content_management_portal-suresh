import pytest
from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.delete_clean_solution_interactor\
    import DeleteCleanSolutionInteractor
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_delete_clean_solution_interactor_with_invalid_question_id_raises_error():
    # Arrange
    clean_solution_id = 1
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteCleanSolutionInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = False
    clean_solution_storage.is_valid_clean_solution_id.return_value = True
    clean_solution_storage.\
        is_clean_solution_belongs_to_question.return_value = True
    presenter.raise_invalid_question_id_exception.side_effect = NotFound
    clean_solution_storage.delete_clean_solution.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_clean_solution(
            clean_solution_id=clean_solution_id, question_id=question_id
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.delete_clean_solution.assert_not_called()


def test_delete_clean_solution_interactor_with_invalid_clean_solution_id_raises_error():
    # Arrange
    clean_solution_id = 1
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteCleanSolutionInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    clean_solution_storage.is_valid_clean_solution_id.return_value = False
    clean_solution_storage.\
        is_clean_solution_belongs_to_question.return_value = True
    presenter.raise_invalid_clean_solution_id_exception.side_effect = NotFound
    clean_solution_storage.delete_clean_solution.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_clean_solution(
            clean_solution_id=clean_solution_id, question_id=question_id
        )

    # Assert
    clean_solution_storage.is_valid_clean_solution_id.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    clean_solution_storage.delete_clean_solution.assert_not_called()


def test_delete_clean_solution_interactor_with_clean_solution_not_belong_to_question_raises_error():
    # Arrange
    clean_solution_id = 1
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteCleanSolutionInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    clean_solution_storage.is_valid_clean_solution_id.return_value = True
    clean_solution_storage.\
        is_clean_solution_belongs_to_question.return_value = False
    presenter.raise_clean_solution_not_belongs_to_question_exception.side_effect = \
        BadRequest
    clean_solution_storage.delete_clean_solution.return_value = None

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_clean_solution(
            clean_solution_id=clean_solution_id, question_id=question_id
        )

    # Assert
    clean_solution_storage.is_valid_clean_solution_id.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    clean_solution_storage.delete_clean_solution.assert_not_called()


def test_delete_clean_solution_interactor_with_valid_details():
    # Arrange
    clean_solution_id = 1
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteCleanSolutionInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    clean_solution_storage.is_valid_clean_solution_id.return_value = True
    clean_solution_storage.\
        is_clean_solution_belongs_to_question.return_value = True
    clean_solution_storage.delete_clean_solution.return_value = None

    # Act
    interactor.delete_clean_solution(
        clean_solution_id=clean_solution_id,
        question_id=question_id
    )

    # Assert
    clean_solution_storage.is_valid_clean_solution_id.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    clean_solution_storage.delete_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
