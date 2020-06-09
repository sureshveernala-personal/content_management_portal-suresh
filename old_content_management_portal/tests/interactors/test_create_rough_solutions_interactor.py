from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_rough_solutions_interactor\
    import CreateRoughSolutionsInteractor


def test_create_rough_solution_interactor_with_invalid_question_id_raises_error(rough_solution_dicts):
    # Arrange
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_rough_solutions(
            question_id=question_id, rough_solutions=rough_solution_dicts
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_rough_solution_interactor_with_invalid_rough_solution_id_raises_error(
        rough_solution_dicts
    ):
    # Arrange
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    rough_solution_storage.get_rough_solution_ids.return_value = [2]
    rough_solution_storage.get_question_rough_solution_ids.return_value = [1]
    presenter.raise_invalid_rough_solution_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_rough_solutions(
            question_id=question_id, rough_solutions=rough_solution_dicts
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.get_rough_solution_ids.assert_called_once()
    rough_solution_storage.get_question_rough_solution_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_rough_solution_interactor_with_invalid_questions_rough_solution_raises_error(
        rough_solution_dicts
    ):
    # Arrange
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    rough_solution_storage.get_rough_solution_ids.return_value = [1]
    rough_solution_storage.get_question_rough_solution_ids.return_value = [2]
    presenter.raise_rough_solution_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_rough_solutions(
            question_id=question_id, rough_solutions=rough_solution_dicts
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.get_rough_solution_ids.assert_called_once()
    rough_solution_storage.get_question_rough_solution_ids.\
        assert_called_once_with(question_id=question_id)


def test_create_rough_solution_interactor_with_valid_details(
        rough_solution_dicts, rough_solution_dtos,
        rough_solution_with_question_id_dicts,
        rough_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    rough_solution_storage.get_rough_solution_ids.return_value = [1]
    rough_solution_storage.get_question_rough_solution_ids.return_value = [1]
    rough_solution_storage.update_rough_solutions.return_value = None
    rough_solution_storage.create_rough_solutions.return_value = None
    rough_solution_storage.get_rough_solutions.return_value = \
        rough_solution_with_question_id_dtos
    presenter.get_create_rough_solutions_response.return_value =\
        rough_solution_with_question_id_dtos

    # Act
    response = interactor.create_rough_solutions(
        question_id=question_id, rough_solutions=rough_solution_dicts
    )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.get_rough_solution_ids.assert_called_once()
    rough_solution_storage.get_question_rough_solution_ids.\
        assert_called_once_with(question_id=question_id)
    rough_solution_storage.get_rough_solutions.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.update_rough_solutions.assert_called_once_with(
        rough_solution_ids=[1], rough_solution_dtos=rough_solution_dtos[:1]
    )
    rough_solution_storage.create_rough_solutions.assert_called_once_with(
        question_id=question_id, rough_solutions_dtos=rough_solution_dtos[1:]
    )
    presenter.get_create_rough_solutions_response.assert_called_once_with(
        rough_solutions_dto_with_question_id=rough_solution_with_question_id_dtos
    )
    assert response == rough_solution_with_question_id_dtos


def test_create_rough_solution_interactor_when_no_new_solutions(
        rough_solution_dicts, rough_solution_dtos,
        rough_solution_with_question_id_dicts,
        rough_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    rough_solution_with_question_id_dtos.rough_solutions = \
        [rough_solution_with_question_id_dtos.rough_solutions[0]]
    rough_solution_with_question_id_dicts['rough_solutions'] = \
        [rough_solution_with_question_id_dicts['rough_solutions'][0]]
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    rough_solution_storage.get_rough_solution_ids.return_value = [1]
    rough_solution_storage.get_question_rough_solution_ids.return_value = [1]
    rough_solution_storage.update_rough_solutions.return_value = None
    rough_solution_storage.create_rough_solutions.return_value = None
    rough_solution_storage.get_rough_solutions.return_value = \
        rough_solution_with_question_id_dtos
    presenter.get_create_rough_solutions_response.return_value =\
        rough_solution_with_question_id_dicts

    # Act
    response = interactor.create_rough_solutions(
        question_id=question_id, rough_solutions=rough_solution_dicts[:1]
    )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.get_rough_solution_ids.assert_called_once()
    rough_solution_storage.get_question_rough_solution_ids.\
        assert_called_once_with(question_id=question_id)
    rough_solution_storage.get_rough_solutions.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.update_rough_solutions.assert_called_once_with(
        rough_solution_ids=[1], rough_solution_dtos=rough_solution_dtos[:1]
    )
    rough_solution_storage.create_rough_solutions.assert_called_once_with(
        question_id=question_id, rough_solutions_dtos=[]
    )
    presenter.get_create_rough_solutions_response.assert_called_once_with(
        rough_solutions_dto_with_question_id=rough_solution_with_question_id_dtos
    )
    assert response == rough_solution_with_question_id_dicts


def test_create_rough_solution_interactor_when_no_upadates(
        rough_solution_dicts, rough_solution_dtos,
        rough_solution_with_question_id_dicts,
        rough_solution_with_question_id_dtos
    ):
    # Arrange
    question_id = 1
    rough_solution_with_question_id_dtos.rough_solutions = \
        [rough_solution_with_question_id_dtos.rough_solutions[1]]
    rough_solution_with_question_id_dicts['rough_solutions'] = \
        [rough_solution_with_question_id_dicts['rough_solutions'][1]]
    rough_solution_storage = create_autospec(RoughSolutionStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRoughSolutionsInteractor(
        rough_solution_storage=rough_solution_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    rough_solution_storage.update_rough_solutions.return_value = None
    rough_solution_storage.create_rough_solutions.return_value = None
    rough_solution_storage.get_rough_solutions.return_value = \
        rough_solution_with_question_id_dtos
    presenter.get_create_rough_solutions_response.return_value =\
        rough_solution_with_question_id_dicts

    # Act
    response = interactor.create_rough_solutions(
        question_id=question_id, rough_solutions=rough_solution_dicts[1:]
    )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.get_rough_solution_ids.assert_called_once()
    rough_solution_storage.get_question_rough_solution_ids.\
        assert_called_once_with(question_id=question_id)
    rough_solution_storage.get_rough_solutions.assert_called_once_with(
        question_id=question_id
    )
    rough_solution_storage.update_rough_solutions.assert_called_once_with(
        rough_solution_ids=[], rough_solution_dtos= []
    )
    rough_solution_storage.create_rough_solutions.assert_called_once_with(
        question_id=1, rough_solutions_dtos=rough_solution_dtos[1:]
    )
    presenter.get_create_rough_solutions_response.assert_called_once_with(
        rough_solutions_dto_with_question_id=rough_solution_with_question_id_dtos
    )
    assert response == rough_solution_with_question_id_dicts
