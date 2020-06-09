import pytest
from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.delete_hint_interactor\
    import DeleteHintInteractor
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_delete_hint_interactor_with_invalid_question_id_raises_error():
    # Arrange
    hint_id = 1
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.\
        is_hint_belongs_to_question.return_value = True
    presenter.raise_invalid_question_id_exception.side_effect = NotFound
    hint_storage.delete_hint.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_hint(
            hint_id=hint_id, question_id=question_id
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.delete_hint.assert_not_called()


def test_delete_hint_interactor_with_invalid_hint_id_raises_error():
    # Arrange
    hint_id = 1
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = False
    hint_storage.\
        is_hint_belongs_to_question.return_value = True
    presenter.raise_invalid_hint_id_exception.side_effect = NotFound
    hint_storage.delete_hint.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_hint(
            hint_id=hint_id, question_id=question_id
        )

    # Assert
    hint_storage.is_valid_hint_id.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.delete_hint.assert_not_called()


def test_delete_hint_interactor_with_hint_not_belong_to_question_raises_error():
    # Arrange
    hint_id = 1
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.\
        is_hint_belongs_to_question.return_value = False
    presenter.raise_hint_not_belongs_to_question_exception.side_effect = \
        BadRequest
    hint_storage.delete_hint.return_value = None

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_hint(
            hint_id=hint_id, question_id=question_id
        )

    # Assert
    hint_storage.is_valid_hint_id.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.delete_hint.assert_not_called()


def test_delete_hint_interactor_with_valid_details():
    # Arrange
    hint_id = 1
    question_id = 1
    hint_number = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.\
        is_hint_belongs_to_question.return_value = True
    hint_storage.delete_hint.return_value = hint_number

    # Act
    interactor.delete_hint(
        hint_id=hint_id,
        question_id=question_id
    )

    # Assert
    hint_storage.is_valid_hint_id.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.delete_hint.assert_called_once_with(
        hint_id=hint_id, question_id=question_id
    )
    hint_storage.decrease_hint_numbers_followed_given_hint_number.\
        assert_called_once_with(question_id=1,hint_number=hint_number)
