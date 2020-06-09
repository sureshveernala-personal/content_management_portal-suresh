from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_hint_interactor\
    import CreateHintInteractor


def test_create_hint_interactor_with_invalid_question_id_raises_error(
        hint_dict
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    hint_storage.get_max_hint_number.return_value = None
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_hint(
            question_id=question_id, hint_details=hint_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_hint_interactor_with_invalid_hint_id_raises_error(
        hint_dict
    ):
    # Arrange
    question_id = 1
    hint_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = False
    hint_storage.get_max_hint_number.return_value = None
    presenter.raise_invalid_hint_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_hint(
            question_id=question_id, hint_details=hint_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.is_valid_hint_id.assert_called_once_with(
        hint_id=hint_id
    )


def test_create_hint_interactor_when_hint_not_belongs_to_question_raises_error(
        hint_dict
    ):
    # Arrange
    question_id = 1
    hint_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.is_hint_belongs_to_question.return_value = False
    hint_storage.get_max_hint_number.return_value = None
    presenter.raise_hint_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_hint(
            question_id=question_id, hint_details=hint_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.is_valid_hint_id.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.is_hint_belongs_to_question.assert_called_once_with(
        hint_id=hint_id, question_id=question_id
    )


def test_create_hint_interactor_without_giving_hint_id_return_dict(
        hint_dict_without_hint_id,
        hint_dto_without_hint_id,
        hint_with_question_id_dict, hint_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    hint_storage.get_max_hint_number.return_value = None
    question_storage.is_valid_question_id.return_value = True
    hint_storage.create_hint.return_value = \
        hint_with_question_id_dto
    presenter.get_create_hint_response.return_value = \
        hint_with_question_id_dict

    # Act
    response = interactor.create_hint(
        question_id=question_id,
        hint_details=hint_dict_without_hint_id
    )

    # Assert
    assert response == hint_with_question_id_dict
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.is_valid_hint_id.assert_not_called()
    hint_storage.create_hint.assert_called_once_with(
        question_id=question_id,
        hint_details=hint_dto_without_hint_id
    )

def test_create_hint_interactor_by_giving_hint_id_return_dict(
        hint_dict, hint_dto,
        hint_with_question_id_dict, hint_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    hint_id = 1
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    hint_storage.get_max_hint_number.return_value = None
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.is_hint_belongs_to_question.return_value = True
    hint_storage.create_hint.return_value = \
        hint_with_question_id_dto
    presenter.get_create_hint_response.return_value = \
        hint_with_question_id_dict

    # Act
    response = interactor.create_hint(
        question_id=question_id,
        hint_details=hint_dict
    )

    # Assert
    assert response == hint_with_question_id_dict
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.update_hint.assert_called_once_with(
        hint_details=hint_dto
    )


def test_create_hint_interactor_by_giving_hint_id_when_question_has_hints_return_dict(
        hint_dict, hint_dto,
        hint_with_question_id_dict, hint_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    hint_id = 1
    hint_dto.hint_number = 2
    hint_with_question_id_dto.hint_number = 2
    hint_storage = create_autospec(HintStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    hint_storage.get_max_hint_number.return_value = 1
    question_storage.is_valid_question_id.return_value = True
    hint_storage.is_valid_hint_id.return_value = True
    hint_storage.is_hint_belongs_to_question.return_value = True
    hint_storage.create_hint.return_value = \
        hint_with_question_id_dto
    presenter.get_create_hint_response.return_value = \
        hint_with_question_id_dict

    # Act
    response = interactor.create_hint(
        question_id=question_id,
        hint_details=hint_dict
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.update_hint.assert_called_once_with(
        hint_details=hint_dto
    )
    assert response == hint_with_question_id_dict
