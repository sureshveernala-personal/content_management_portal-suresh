import pytest
from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.delete_rough_solution_interactor\
    import DeleteRoughSolutionInteractor
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_delete_rough_solution_interactor_with_invalid_question_id_raises_error():
    # Arrange
    rough_solution_id = 1
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRoughSolutionInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    rough_solution_storage.is_valid_rough_solution_id.return_value = True
    rough_solution_storage.\
        is_rough_solution_belongs_to_question.return_value = True
    presenter.raise_invalid_question_id_exception.side_effect = NotFound
    rough_solution_storage.delete_rough_solution.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_rough_solution(
            rough_solution_id=rough_solution_id, question_id=question_id
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.delete_rough_solution.assert_not_called()


def test_delete_rough_solution_interactor_with_invalid_rough_solution_id_raises_error():
    # Arrange
    rough_solution_id = 1
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRoughSolutionInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    rough_solution_storage.is_valid_rough_solution_id.return_value = False
    rough_solution_storage.\
        is_rough_solution_belongs_to_question.return_value = True
    presenter.raise_invalid_rough_solution_exception.side_effect = NotFound
    rough_solution_storage.delete_rough_solution.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_rough_solution(
            rough_solution_id=rough_solution_id, question_id=question_id
        )

    # Assert
    rough_solution_storage.is_valid_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    rough_solution_storage.delete_rough_solution.assert_not_called()


def test_delete_rough_solution_interactor_with_rough_solution_not_belong_to_question_raises_error():
    # Arrange
    rough_solution_id = 1
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRoughSolutionInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    rough_solution_storage.is_valid_rough_solution_id.return_value = True
    rough_solution_storage.\
        is_rough_solution_belongs_to_question.return_value = False
    presenter.raise_rough_solution_not_belongs_to_question_exception.side_effect = \
        BadRequest
    rough_solution_storage.delete_rough_solution.return_value = None

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_rough_solution(
            rough_solution_id=rough_solution_id, question_id=question_id
        )

    # Assert
    rough_solution_storage.is_valid_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    rough_solution_storage.delete_rough_solution.assert_not_called()


def test_delete_rough_solution_interactor_with_valid_details():
    # Arrange
    rough_solution_id = 1
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRoughSolutionInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    rough_solution_storage.is_valid_rough_solution_id.return_value = True
    rough_solution_storage.\
        is_rough_solution_belongs_to_question.return_value = True
    rough_solution_storage.delete_rough_solution.return_value = None

    # Act
    interactor.delete_rough_solution(
        rough_solution_id=rough_solution_id,
        question_id=question_id
    )

    # Assert
    rough_solution_storage.is_valid_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    rough_solution_storage.delete_rough_solution.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
