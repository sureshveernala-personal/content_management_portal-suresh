from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_prefilled_codes_interactor\
    import CreatePrefilledCodesInteractor


def test_create_prefilled_code_interactor_with_invalid_question_id_raises_error(
        prefilled_code_dicts
    ):
    # Arrange
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_prefilled_codes(
            question_id=question_id, prefilled_codes=prefilled_code_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_prefilled_code_interactor_with_invalid_prefilled_code_id_raises_error(
        prefilled_code_dicts
    ):
    # Arrange
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.get_prefilled_code_ids.return_value = [2]
    prefilled_code_storage.get_question_prefilled_code_ids.return_value = [1]
    presenter.raise_invalid_prefilled_code_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_prefilled_codes(
            question_id=question_id, prefilled_codes=prefilled_code_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_prefilled_code_ids.assert_called_once()
    prefilled_code_storage.get_question_prefilled_code_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_prefilled_code_interactor_with_invalid_questions_prefilled_code_raises_error(
        prefilled_code_dicts
    ):
    # Arrange
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.get_prefilled_code_ids.return_value = [1]
    prefilled_code_storage.get_question_prefilled_code_ids.return_value = [2]
    presenter.raise_prefilled_code_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_prefilled_codes(
            question_id=question_id, prefilled_codes=prefilled_code_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_prefilled_code_ids.assert_called_once()
    prefilled_code_storage.get_question_prefilled_code_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_prefilled_code_interactor_with_valid_details(
        prefilled_code_dicts, prefilled_code_dtos,
        prefilled_code_with_question_id_dicts,
        prefilled_code_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.get_prefilled_code_ids.return_value = [1]
    prefilled_code_storage.get_question_prefilled_code_ids.return_value = [1]
    prefilled_code_storage.update_prefilled_codes.return_value = None
    prefilled_code_storage.create_prefilled_codes.return_value = None
    prefilled_code_storage.get_prefilled_codes.return_value = \
        prefilled_code_with_question_id_dtos
    presenter.get_create_prefilled_codes_response.return_value =\
        prefilled_code_with_question_id_dtos

    # Act
    response = interactor.create_prefilled_codes(
        question_id=question_id, prefilled_codes=prefilled_code_dicts
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_prefilled_code_ids.assert_called_once()
    prefilled_code_storage.get_question_prefilled_code_ids.\
        assert_called_once_with(question_id=question_id)
    prefilled_code_storage.get_prefilled_codes.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.update_prefilled_codes.assert_called_once_with(
        prefilled_code_ids=[1], prefilled_code_dtos=prefilled_code_dtos[:1]
    )
    prefilled_code_storage.create_prefilled_codes.assert_called_once_with(
        question_id=question_id, prefilled_code_dtos=prefilled_code_dtos[1:]
    )
    presenter.get_create_prefilled_codes_response.assert_called_once_with(
        question_id=question_id,
        prefilled_code_with_question_id_dtos=prefilled_code_with_question_id_dtos
    )
    assert response == prefilled_code_with_question_id_dtos


def test_create_prefilled_code_interactor_when_no_new_solutions(
        prefilled_code_dicts, prefilled_code_dtos,
        prefilled_code_with_question_id_dicts,
        prefilled_code_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    prefilled_code_with_question_id_dtos = \
        [prefilled_code_with_question_id_dtos[0]]
    prefilled_code_with_question_id_dicts['prefilled_codes'] = \
        [prefilled_code_with_question_id_dicts['prefilled_codes'][0]]
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.get_prefilled_code_ids.return_value = [1]
    prefilled_code_storage.get_question_prefilled_code_ids.return_value = [1]
    prefilled_code_storage.update_prefilled_codes.return_value = None
    prefilled_code_storage.create_prefilled_codes.return_value = None
    prefilled_code_storage.get_prefilled_codes.return_value = \
        prefilled_code_with_question_id_dtos
    presenter.get_create_prefilled_codes_response.return_value =\
        prefilled_code_with_question_id_dicts

    # Act
    response = interactor.create_prefilled_codes(
        question_id=question_id, prefilled_codes=prefilled_code_dicts[:1]
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_prefilled_code_ids.assert_called_once()
    prefilled_code_storage.get_question_prefilled_code_ids.\
        assert_called_once_with(question_id=question_id)
    prefilled_code_storage.get_prefilled_codes.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.update_prefilled_codes.assert_called_once_with(
        prefilled_code_ids=[1], prefilled_code_dtos=prefilled_code_dtos[:1]
    )
    prefilled_code_storage.create_prefilled_codes.assert_called_once_with(
        question_id=question_id, prefilled_code_dtos=[]
    )
    presenter.get_create_prefilled_codes_response.assert_called_once_with(
        question_id=question_id,
        prefilled_code_with_question_id_dtos=prefilled_code_with_question_id_dtos
    )
    assert response == prefilled_code_with_question_id_dicts


def test_create_prefilled_code_interactor_when_no_upadates(
        prefilled_code_dicts, prefilled_code_dtos,
        prefilled_code_with_question_id_dicts,
        prefilled_code_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    prefilled_code_with_question_id_dtos = \
        [prefilled_code_with_question_id_dtos[1]]
    prefilled_code_with_question_id_dicts['prefilled_codes'] = \
        [prefilled_code_with_question_id_dicts['prefilled_codes'][1]]
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePrefilledCodesInteractor(
        prefilled_code_storage=prefilled_code_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    prefilled_code_storage.update_prefilled_codes.return_value = None
    prefilled_code_storage.create_prefilled_codes.return_value = None
    prefilled_code_storage.get_prefilled_codes.return_value = \
        prefilled_code_with_question_id_dtos
    presenter.get_create_prefilled_codes_response.return_value =\
        prefilled_code_with_question_id_dicts

    # Act
    response = interactor.create_prefilled_codes(
        question_id=question_id, prefilled_codes=prefilled_code_dicts[1:]
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_prefilled_code_ids.assert_called_once()
    prefilled_code_storage.get_question_prefilled_code_ids.\
        assert_called_once_with(question_id=question_id)
    prefilled_code_storage.get_prefilled_codes.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.update_prefilled_codes.assert_called_once_with(
        prefilled_code_ids=[], prefilled_code_dtos= []
    )
    prefilled_code_storage.create_prefilled_codes.assert_called_once_with(
        question_id=1, prefilled_code_dtos=prefilled_code_dtos[1:]
    )
    presenter.get_create_prefilled_codes_response.assert_called_once_with(
        question_id=question_id,
        prefilled_code_with_question_id_dtos=prefilled_code_with_question_id_dtos
    )
    assert response == prefilled_code_with_question_id_dicts
