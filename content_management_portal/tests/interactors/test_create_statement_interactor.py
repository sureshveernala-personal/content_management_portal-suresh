from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_problem_statement_interactor\
    import CreateProblemStatementInteractor
from django_swagger_utils.drf_server.exceptions import NotFound
import pytest


def test_create_statement_interactor_with_invalid_question_id_raises_error(
        description_dto):
    # Arrange
    user_id = 1
    short_text = "string"
    question_id =1
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.\
        side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_problem_statement_wrapper(
            user_id=user_id, short_text=short_text,
            description_dto=description_dto, question_id=question_id,
            presenter=presenter
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_statement_interactor_with_new_data_returns_question_id(
        description_dto, question_dto, question_dict
    ):
    # Arrange
    user_id = 1
    short_text = "string"
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    question_storage.create_problem_statement.return_value = \
        question_dto
    presenter.get_create_problem_statement_response.return_value =\
        question_dict

    # Act
    response = interactor.create_problem_statement_wrapper(
        user_id=user_id, short_text=short_text, presenter=presenter,
        description_dto=description_dto, question_id=None
    )

    # Assert
    question_storage.create_problem_statement.assert_called_once_with(
        user_id=user_id, short_text=short_text,
        description=description_dto
    )
    presenter.get_create_problem_statement_response.assert_called_once_with(
        question_dto=question_dto
    )
    assert response == question_dict


def test_create_statement_interactor_with_existing_question_id_returns_question_id(
        description_dto, question_dto, question_dict
    ):
    # Arrange
    user_id = 1
    question_id = 1
    short_text = "string"
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    question_storage.update_problem_statement.return_value = \
        question_dto
    presenter.get_create_problem_statement_response.return_value =\
        question_dict

    # Act
    response = interactor.create_problem_statement_wrapper(
        user_id=user_id, short_text=short_text, presenter=presenter,
        description_dto=description_dto, question_id=question_id
    )

    # Assert
    question_storage.update_problem_statement.assert_called_once_with(
        user_id=user_id, short_text=short_text,
        description=description_dto, question_id=question_id
    )
    presenter.get_create_problem_statement_response.assert_called_once_with(
        question_dto=question_dto
    )
    assert response == question_dict
