import pytest
from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.delete_prefilled_code_interactor\
    import DeletePrefilledCodeInteractor
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_delete_prefilled_code_interactor_with_invalid_question_id_raises_error():
    # Arrange
    prefilled_code_id = 1
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePrefilledCodeInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    prefilled_code_storage.is_valid_prefilled_code_id.return_value = True
    prefilled_code_storage.\
        is_prefilled_code_belongs_to_question.return_value = True
    presenter.raise_invalid_question_id_exception.side_effect = NotFound
    prefilled_code_storage.delete_prefilled_code.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_prefilled_code(
            prefilled_code_id=prefilled_code_id, question_id=question_id
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.delete_prefilled_code.assert_not_called()


def test_delete_prefilled_code_interactor_with_invalid_prefilled_code_id_raises_error():
    # Arrange
    prefilled_code_id = 1
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePrefilledCodeInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.is_valid_prefilled_code_id.return_value = False
    prefilled_code_storage.\
        is_prefilled_code_belongs_to_question.return_value = True
    presenter.raise_invalid_prefilled_code_id_exception.side_effect = NotFound
    prefilled_code_storage.delete_prefilled_code.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_prefilled_code(
            prefilled_code_id=prefilled_code_id, question_id=question_id
        )

    # Assert
    prefilled_code_storage.is_valid_prefilled_code_id.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    prefilled_code_storage.delete_prefilled_code.assert_not_called()


def test_delete_prefilled_code_interactor_with_prefilled_code_not_belong_to_question_raises_error():
    # Arrange
    prefilled_code_id = 1
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePrefilledCodeInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.is_valid_prefilled_code_id.return_value = True
    prefilled_code_storage.\
        is_prefilled_code_belongs_to_question.return_value = False
    presenter.raise_prefilled_code_not_belongs_to_question_exception.side_effect = \
        BadRequest
    prefilled_code_storage.delete_prefilled_code.return_value = None

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_prefilled_code(
            prefilled_code_id=prefilled_code_id, question_id=question_id
        )

    # Assert
    prefilled_code_storage.is_valid_prefilled_code_id.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    prefilled_code_storage.delete_prefilled_code.assert_not_called()


def test_delete_prefilled_code_interactor_with_valid_details():
    # Arrange
    prefilled_code_id = 1
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePrefilledCodeInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.is_valid_prefilled_code_id.return_value = True
    prefilled_code_storage.\
        is_prefilled_code_belongs_to_question.return_value = True
    prefilled_code_storage.delete_prefilled_code.return_value = None

    # Act
    interactor.delete_prefilled_code(
        prefilled_code_id=prefilled_code_id,
        question_id=question_id
    )

    # Assert
    prefilled_code_storage.is_valid_prefilled_code_id.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    prefilled_code_storage.delete_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
