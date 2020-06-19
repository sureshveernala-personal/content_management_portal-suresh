from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
import pytest
from unittest.mock import create_autospec
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.\
    fill_in_blanks_submit_form_response_interactor import\
    FillInBlanksSubmitFormResponseInteractor
from formaster.exceptions.exceptions import InvalidUserResponse
from formaster.interactors.storages.dtos import FormDto


def test_fill_in_blanks_submit_form_response_interactor_with_valid_details(
        form_dto, fill_in_blanks_response_dto
    ):
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    response_text = "response_text"
    response_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = FillInBlanksSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id, response_text=response_text

    )
    storage.get_form.return_value = form_dto
    storage.is_valid_question_id.return_value = True
    storage.is_question_id_belongs_form.return_value = True
    storage.is_option_id_belongs_to_question.return_value = True
    storage.create_user_fill_in_blanks_response.return_value = response_id
    presenter.get_submit_form_response.return_value = "response"

    # Act
    response = interactor.sumbit_form_response_wrapper(presenter=presenter)

    # Assert
    kwargs = storage.create_user_fill_in_blanks_response.call_args.kwargs
    actual_fill_in_blanks_response_dto = kwargs['fill_in_blanks_response_dto']
    assert actual_fill_in_blanks_response_dto.response_text == response_text
    assert actual_fill_in_blanks_response_dto.question_id == question_id
    assert actual_fill_in_blanks_response_dto.user_id == user_id
    presenter.get_submit_form_response.assert_called_once_with(
        response_id=response_id
    )
    assert response == "response"
