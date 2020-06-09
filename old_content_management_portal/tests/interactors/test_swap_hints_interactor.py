from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.swap_hints_interactor\
    import SwapHintsInteractor


def test_create_hint_interactor_with_invalid_question_id_raises_error(
        hints_swap_details_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_hints(
            question_id=question_id,
            hints_swap_details=hints_swap_details_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_not_called()


def test_create_hint_interactor_with_invalid_first_hint_id_raises_error(
        hints_swap_details_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    hint_storage.get_hint_ids.return_value = [2]
    hint_storage.get_given_question_hint_ids.return_value = [1, 2]
    presenter.raise_invalid_hint_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_hints(
            question_id=question_id,
            hints_swap_details=hints_swap_details_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_not_called()

def test_create_hint_interactor_with_invalid_second_hint_id_raises_error(
        hints_swap_details_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    hint_storage.get_hint_ids.return_value = [1]
    hint_storage.get_given_question_hint_ids.return_value = [1, 2]
    presenter.raise_invalid_hint_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_hints(
            question_id=question_id,
            hints_swap_details=hints_swap_details_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_not_called()

def test_create_hint_interactor_when_first_hint_id_not_belongs_to_raises_error(
        hints_swap_details_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    hint_storage.get_hint_ids.return_value = [1, 2]
    hint_storage.get_given_question_hint_ids.return_value = [2]
    presenter.raise_hint_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.swap_hints(
            question_id=question_id,
            hints_swap_details=hints_swap_details_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_not_called()


def test_create_hint_interactor_when_second_hint_id_not_belongs_to_raises_error(
        hints_swap_details_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    hint_storage.get_hint_ids.return_value = [1, 2]
    hint_storage.get_given_question_hint_ids.return_value = [1]
    presenter.raise_hint_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.swap_hints(
            question_id=question_id,
            hints_swap_details=hints_swap_details_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_not_called()


def test_create_hint_interactor_with_with_valid_details(
        hints_swap_details_dict, hints_swap_details_dto
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    hint_storage.get_hint_ids.return_value = [1, 2]
    hint_storage.get_given_question_hint_ids.return_value = [1, 2]
    presenter.raise_hint_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    interactor.swap_hints(
        question_id=question_id,
        hints_swap_details=hints_swap_details_dict
    )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.swap_hints.assert_called_with(
        hints_swap_details=hints_swap_details_dto
    )
