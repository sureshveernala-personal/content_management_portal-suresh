from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_clean_solutions_interactor\
    import CreateCleanSolutionsInteractor


def test_create_clean_solution_interactor_with_invalid_question_id_raises_error(
        clean_solution_dicts
    ):
    # Arrange
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_clean_solutions(
            question_id=question_id, clean_solutions=clean_solution_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_clean_solution_interactor_with_invalid_clean_solution_id_raises_error(
        clean_solution_dicts
    ):
    # Arrange
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [2]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    presenter.raise_invalid_clean_solution_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_clean_solutions(
            question_id=question_id, clean_solutions=clean_solution_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_clean_solution_interactor_with_invalid_questions_clean_solution_raises_error(
        clean_solution_dicts
    ):
    # Arrange
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [2]
    presenter.raise_clean_solution_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_clean_solutions(
            question_id=question_id, clean_solutions=clean_solution_dicts
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_clean_solution_interactor_with_valid_details(
        clean_solution_dicts, clean_solution_dtos,
        clean_solution_with_question_id_dicts,
        clean_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solutions.return_value = \
        clean_solution_with_question_id_dtos
    presenter.get_create_clean_solutions_response.return_value =\
        clean_solution_with_question_id_dtos

    # Act
    response = interactor.create_clean_solutions(
        question_id=question_id, clean_solutions=clean_solution_dicts
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)
    clean_solution_storage.get_clean_solutions.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.update_clean_solutions.assert_called_once_with(
        clean_solution_ids=[1], clean_solution_dtos=clean_solution_dtos[:1]
    )
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        question_id=question_id, clean_solution_dtos=clean_solution_dtos[1:]
    )
    presenter.get_create_clean_solutions_response.assert_called_once_with(
        question_id=question_id,
        clean_solution_with_question_id_dtos=clean_solution_with_question_id_dtos
    )
    assert response == clean_solution_with_question_id_dtos


def test_create_clean_solution_interactor_when_no_new_solutions(
        clean_solution_dicts, clean_solution_dtos,
        clean_solution_with_question_id_dicts,
        clean_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    clean_solution_with_question_id_dtos = \
        [clean_solution_with_question_id_dtos[0]]
    clean_solution_with_question_id_dicts['clean_solutions'] = \
        [clean_solution_with_question_id_dicts['clean_solutions'][0]]
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solutions.return_value = \
        clean_solution_with_question_id_dtos
    presenter.get_create_clean_solutions_response.return_value =\
        clean_solution_with_question_id_dicts

    # Act
    response = interactor.create_clean_solutions(
        question_id=question_id, clean_solutions=clean_solution_dicts[:1]
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)
    clean_solution_storage.get_clean_solutions.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.update_clean_solutions.assert_called_once_with(
        clean_solution_ids=[1], clean_solution_dtos=clean_solution_dtos[:1]
    )
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        question_id=question_id, clean_solution_dtos=[]
    )
    presenter.get_create_clean_solutions_response.assert_called_once_with(
        question_id=question_id,
        clean_solution_with_question_id_dtos=clean_solution_with_question_id_dtos
    )
    assert response == clean_solution_with_question_id_dicts


def test_create_clean_solution_interactor_when_no_upadates(
        clean_solution_dicts, clean_solution_dtos,
        clean_solution_with_question_id_dicts,
        clean_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    clean_solution_with_question_id_dtos = \
        [clean_solution_with_question_id_dtos[1]]
    clean_solution_with_question_id_dicts['clean_solutions'] = \
        [clean_solution_with_question_id_dicts['clean_solutions'][1]]
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solutions.return_value = \
        clean_solution_with_question_id_dtos
    presenter.get_create_clean_solutions_response.return_value =\
        clean_solution_with_question_id_dicts

    # Act
    response = interactor.create_clean_solutions(
        question_id=question_id, clean_solutions=clean_solution_dicts[1:]
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)
    clean_solution_storage.get_clean_solutions.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.update_clean_solutions.assert_called_once_with(
        clean_solution_ids=[], clean_solution_dtos= []
    )
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        question_id=1, clean_solution_dtos=clean_solution_dtos[1:]
    )
    presenter.get_create_clean_solutions_response.assert_called_once_with(
        question_id=question_id,
        clean_solution_with_question_id_dtos=clean_solution_with_question_id_dtos
    )
    assert response == clean_solution_with_question_id_dicts
