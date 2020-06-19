from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
import pytest
from unittest.mock import create_autospec
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.base_submit_form_response_interactor import\
    BaseSubmitFormResponseInteractor
from formaster.exceptions.exceptions import InvalidFormId, FormClosed,\
    InvalidQuestionId, QuestionIdNotBelongsToForm
from formaster.interactors.storages.dtos import FormDto


def test_base_submit_form_response_interactor_with_invalid_form_id():
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id
    )
    storage.get_form.side_effect = InvalidFormId
    presenter.raise_invalid_form_id_exception.side_effect = NotFound


    with pytest.raises(NotFound):
        interactor.sumbit_form_response_wrapper(presenter=presenter)


def test_base_submit_form_response_interactor_when_from_closed():
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    form_dto = FormDto(form_id=1, is_live=False)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id
    )
    storage.get_form.return_value = form_dto
    presenter.raise_form_closed_exception.side_effect = BadRequest


    with pytest.raises(BadRequest):
        interactor.sumbit_form_response_wrapper(presenter=presenter)


def test_base_submit_form_response_interactor_with_invalid_question_id(
        form_dto
    ):
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id
    )
    storage.get_form.return_value = form_dto
    storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound


    with pytest.raises(NotFound):
        interactor.sumbit_form_response_wrapper(presenter=presenter)


def test_base_submit_form_response_interactor_when_question_id_not_belongs_form(
        form_dto
    ):
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage, user_id=user_id, question_id=question_id,
        form_id=form_id
    )
    storage.get_form.return_value = form_dto
    storage.is_valid_question_id.return_value = True
    storage.is_question_id_belongs_form.return_value = False
    presenter.raise_question_not_belongs_to_question_exception.side_effect = \
        BadRequest


    with pytest.raises(BadRequest):
        interactor.sumbit_form_response_wrapper(presenter=presenter)
