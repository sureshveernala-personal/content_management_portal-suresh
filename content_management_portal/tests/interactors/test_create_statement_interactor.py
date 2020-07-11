from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import CreateProblemStatementPresenterInterface
from content_management_portal.interactors.create_problem_statement_interactor\
    import CreateProblemStatementInteractor
from django_swagger_utils.drf_server.exceptions import NotFound
import pytest


def test_create_statement_interactor_with_invalid_question_id_raises_error(
        description_dict):
    # Arrange
    user_id = 1
    short_text = "string"
    question_id =1
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(CreateProblemStatementPresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.\
        side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_problem_statement(
            user_id=user_id, short_text=short_text,
            description=description_dict, question_id=question_id
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_statement_interactor_with_new_data_returns_question_id(
        description_dict, description_dto, question_dto, question_dict
    ):
    # Arrange
    user_id = 1
    short_text = "string"
    interactor_question_dto = question_dto
    interactor_question_dto.question_id = None
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(CreateProblemStatementPresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    question_storage.is_valid_question_id.return_value = True
    question_storage.create_problem_statement.return_value = \
        question_dto
    presenter.get_create_problem_statement_response.return_value =\
        question_dict

    # Act
    response = interactor.create_problem_statement(
        user_id=user_id, short_text=short_text,
        description=description_dict, question_id=None
    )

    # Assert
    question_storage.create_problem_statement.assert_called_once_with(
        user_id=user_id, question_dto=question_dto
    )
    presenter.get_create_problem_statement_response.assert_called_once_with(
        question_dto=question_dto
    )
    assert response == question_dict


def test_create_statement_interactor_with_existing_question_id_returns_question_id(
        description_dict, description_dto, question_dto, question_dict
    ):
    # Arrange
    user_id = 1
    question_id = 1
    short_text = "string"
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(CreateProblemStatementPresenterInterface)
    interactor = CreateProblemStatementInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    question_storage.is_valid_question_id.return_value = True
    question_storage.update_problem_statement.return_value = \
        question_dto
    presenter.get_create_problem_statement_response.return_value =\
        question_dict

    # Act
    response = interactor.create_problem_statement(
        user_id=user_id, short_text=short_text,
        description=description_dict, question_id=question_id
    )

    # Assert
    question_storage.update_problem_statement.assert_called_once_with(
        user_id=user_id, question_dto=question_dto
    )
    presenter.get_create_problem_statement_response.assert_called_once_with(
        question_dto=question_dto
    )
    assert response == question_dict
