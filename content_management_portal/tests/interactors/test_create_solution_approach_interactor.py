from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    solution_approach_storage_interface import SolutionApproachStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_solution_approach_interactor\
    import CreateSolutionApproachInteractor


def test_create_solution_approach_interactor_with_invalid_question_id_raises_error(
        solution_approach_dict
    ):
    # Arrange
    question_id = 1
    solution_approach_storage = create_autospec(SolutionApproachStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solution_approach(
            question_id=question_id, solution_approach_details=solution_approach_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_solution_approach_interactor_with_invalid_solution_approach_id_raises_error(
        solution_approach_dict
    ):
    # Arrange
    question_id = 1
    solution_approach_id = 1
    solution_approach_storage = create_autospec(SolutionApproachStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    solution_approach_storage.is_valid_solution_approach_id.return_value = False
    presenter.raise_invalid_solution_approach_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solution_approach(
            question_id=question_id, solution_approach_details=solution_approach_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.is_valid_solution_approach_id.assert_called_once_with(
        solution_approach_id=solution_approach_id
    )


def test_create_solution_approach_interactor_when_solution_approach_not_belongs_to_question_raises_error(
        solution_approach_dict
    ):
    # Arrange
    question_id = 1
    solution_approach_id = 1
    solution_approach_storage = create_autospec(SolutionApproachStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    solution_approach_storage.is_valid_solution_approach_id.return_value = True
    solution_approach_storage.is_solution_approach_belongs_to_question.return_value = False
    presenter.raise_solution_approach_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_solution_approach(
            question_id=question_id, solution_approach_details=solution_approach_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.is_valid_solution_approach_id.assert_called_once_with(
        solution_approach_id=solution_approach_id
    )
    solution_approach_storage.is_solution_approach_belongs_to_question.assert_called_once_with(
        solution_approach_id=solution_approach_id, question_id=question_id
    )


def test_create_solution_approach_interactor_without_giving_solution_approach_id_return_dict(
        solution_approach_dict_without_solution_approach_id,
        solution_approach_dto_without_solution_approach_id,
        solution_approach_with_question_id_dict, solution_approach_dto
    ):
    # Arrange
    question_id = 1
    solution_approach_storage = create_autospec(SolutionApproachStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    solution_approach_storage.create_solution_approach.return_value = \
        solution_approach_dto
    presenter.get_create_solution_approach_response.return_value = \
        solution_approach_with_question_id_dict

    # Act
    response = interactor.create_solution_approach(
        question_id=question_id,
        solution_approach_details=solution_approach_dict_without_solution_approach_id
    )

    # Assert
    assert response == solution_approach_with_question_id_dict
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.is_valid_solution_approach_id.assert_not_called()
    solution_approach_storage.create_solution_approach.assert_called_once_with(
        question_id=question_id,
        solution_approach_details=solution_approach_dto_without_solution_approach_id
    )

def test_create_solution_approach_interactor_by_giving_solution_approach_id_return_dict(
        solution_approach_dict, solution_approach_dto,
        solution_approach_with_question_id_dict
    ):
    # Arrange
    question_id = 1
    solution_approach_id = 1
    solution_approach_storage = create_autospec(SolutionApproachStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    solution_approach_storage.is_valid_solution_approach_id.return_value = True
    solution_approach_storage.is_solution_approach_belongs_to_question.return_value = True
    solution_approach_storage.create_solution_approach.return_value = \
        solution_approach_dto
    presenter.get_create_solution_approach_response.return_value = \
        solution_approach_with_question_id_dict

    # Act
    response = interactor.create_solution_approach(
        question_id=question_id,
        solution_approach_details=solution_approach_dict
    )

    # Assert
    assert response == solution_approach_with_question_id_dict
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.update_solution_approach.assert_called_once_with(
        solution_approach_details=solution_approach_dto
    )
