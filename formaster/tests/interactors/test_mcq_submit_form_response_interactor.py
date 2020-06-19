from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
import pytest
from unittest.mock import create_autospec
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.mcq_question_submit_form_response_interactor import\
    MCQQuestionSubmitFormResponseInteractor
from formaster.exceptions.exceptions import InvalidUserResponse
from formaster.interactors.storages.dtos import FormDto


def test_mcq_submit_form_response_interactor_with_invalid_form_id(form_dto):
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    option_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id, option_id=option_id
    )
    storage.get_form.return_value = form_dto
    storage.is_option_id_belongs_to_question.return_value = False
    storage.is_valid_question_id.return_value = True
    storage.is_question_id_belongs_form.return_value = True
    presenter.raise_invalid_user_response_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.sumbit_form_response_wrapper(presenter=presenter)


def test_mcq_submit_form_response_interactor_with_valid_details(
        form_dto, mcq_response_dto
    ):
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    option_id = 1
    response_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id, option_id=option_id

    )
    storage.get_form.return_value = form_dto
    storage.is_valid_question_id.return_value = True
    storage.is_question_id_belongs_form.return_value = True
    storage.is_option_id_belongs_to_question.return_value = True
    storage.create_user_mcq_response.return_value = response_id
    presenter.get_submit_form_response.return_value = "response"

    # Act
    response = interactor.sumbit_form_response_wrapper(presenter=presenter)

    # Assert
    kwargs = storage.create_user_mcq_response.call_args.kwargs
    actual_mcq_response_dto = kwargs['mcq_response_dto']
    assert actual_mcq_response_dto.option_id == option_id
    assert actual_mcq_response_dto.question_id == question_id
    assert actual_mcq_response_dto.user_id == user_id
    presenter.get_submit_form_response.assert_called_once_with(
        response_id=response_id
    )
    assert response == "response"
