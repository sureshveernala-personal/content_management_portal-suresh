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
        solution_dtos
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
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solutions_wrapper(presenter=presenter)

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_clean_solution_interactor_with_invalid_clean_solution_id_raises_error(
        solution_dtos
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
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [2]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    presenter.raise_invalid_solution_ids_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solutions_wrapper(presenter=presenter)

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()


def test_create_clean_solution_interactor_with_invalid_questions_clean_solution_raises_error(
        solution_dtos
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
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [2]
    presenter.raise_solutions_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solutions_wrapper(presenter=presenter)

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_clean_solution_ids.assert_called_once()
    clean_solution_storage.get_question_clean_solution_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_clean_solution_interactor_with_valid_details(
        solution_dtos, solution_with_question_id_dicts,
        solution_with_question_id_dtos
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
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solutions.return_value = \
        solution_with_question_id_dtos
    presenter.get_create_solutions_response.return_value =\
        solution_with_question_id_dtos

    # Act
    response = interactor.create_solutions_wrapper(presenter=presenter)

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
        clean_solution_ids=[1], clean_solution_dtos=solution_dtos[:1]
    )
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        question_id=question_id, clean_solution_dtos=solution_dtos[1:]
    )
    presenter.get_create_solutions_response.assert_called_once_with(
        question_id=question_id,
        solution_with_question_id_dtos=solution_with_question_id_dtos
    )
    assert response == solution_with_question_id_dtos


def test_create_clean_solution_interactor_when_no_new_solutions(
        solution_dtos,
        solution_with_question_id_dicts,
        solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    solution_with_question_id_dtos = \
        [solution_with_question_id_dtos[0]]
    solution_with_question_id_dicts['solutions'] = \
        [solution_with_question_id_dicts['solutions'][0]]
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos[:1]
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solutions.return_value = \
        solution_with_question_id_dtos
    presenter.get_create_solutions_response.return_value =\
        solution_with_question_id_dicts

    # Act
    response = interactor.create_solutions_wrapper(presenter=presenter)

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
        clean_solution_ids=[1], clean_solution_dtos=solution_dtos[:1]
    )
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        question_id=question_id, clean_solution_dtos=[]
    )
    presenter.get_create_solutions_response.assert_called_once_with(
        question_id=question_id,
        solution_with_question_id_dtos=solution_with_question_id_dtos
    )
    assert response == solution_with_question_id_dicts


def test_create_clean_solution_interactor_when_no_upadates(
        solution_dtos, solution_with_question_id_dicts,
        solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    solution_with_question_id_dtos = \
        [solution_with_question_id_dtos[1]]
    solution_with_question_id_dicts['solutions'] = \
        [solution_with_question_id_dicts['solutions'][1]]
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCleanSolutionsInteractor(
        clean_solution_storage=clean_solution_storage,
        question_storage=question_storage,
        question_id=question_id,
        solution_dtos=solution_dtos[1:]
    )
    question_storage.is_valid_question_id.return_value = True
    clean_solution_storage.update_clean_solutions.return_value = None
    clean_solution_storage.create_clean_solutions.return_value = None
    clean_solution_storage.get_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_question_clean_solution_ids.return_value = [1]
    clean_solution_storage.get_clean_solutions.return_value = \
        solution_with_question_id_dtos
    presenter.get_create_solutions_response.return_value =\
        solution_with_question_id_dicts

    # Act
    response = interactor.create_solutions_wrapper(presenter=presenter)

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
        question_id=1, clean_solution_dtos=solution_dtos[1:]
    )
    presenter.get_create_solutions_response.assert_called_once_with(
        question_id=question_id,
        solution_with_question_id_dtos=solution_with_question_id_dtos
    )
    assert response == solution_with_question_id_dicts
