from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.create_test_case_interactor\
    import CreateTestCaseInteractor
from content_management_portal.interactors.storages.dtos import \
    TestCaseWithQuestionIdDto, TestCaseDto


def test_create_test_case_interactor_with_invalid_question_id_raises_error(
        test_case_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_test_case(
            question_id=question_id, test_case_details=test_case_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )


def test_create_test_case_interactor_with_invalid_test_case_id_raises_error(
        test_case_dict
    ):
    # Arrange
    question_id = 1
    test_case_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = False
    presenter.raise_invalid_test_case_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_test_case(
            question_id=question_id, test_case_details=test_case_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.is_valid_test_case_id.assert_called_once_with(
        test_case_id=test_case_id
    )


def test_create_test_case_interactor_when_test_case_not_belongs_to_question_raises_error(
        test_case_dict
    ):
    # Arrange
    question_id = 1
    test_case_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = True
    test_case_storage.is_test_case_belongs_to_question.return_value = False
    presenter.raise_test_case_not_belongs_to_question_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_test_case(
            question_id=question_id, test_case_details=test_case_dict
        )

    # Assert
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.is_valid_test_case_id.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.is_test_case_belongs_to_question.assert_called_once_with(
        test_case_id=test_case_id, question_id=question_id
    )


def test_create_test_case_interactor_without_giving_test_case_id_return_dict(
        test_case_dict_without_test_case_id,
        test_case_dto_without_test_case_id,
        test_case_with_question_id_dict, test_case_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    test_case_storage.create_test_case.return_value = \
        test_case_with_question_id_dto
    presenter.get_create_test_case_response.return_value = \
        test_case_with_question_id_dict

    # Act
    response = interactor.create_test_case(
        question_id=question_id,
        test_case_details=test_case_dict_without_test_case_id
    )

    # Assert
    assert response == test_case_with_question_id_dict
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.is_valid_test_case_id.assert_not_called()
    test_case_storage.create_test_case.assert_called_once_with(
        question_id=question_id,
        test_case_details=test_case_dto_without_test_case_id
    )

def test_create_test_case_interactor_by_giving_test_case_id_return_dict(
        test_case_dict, test_case_dto,
        test_case_with_question_id_dict, test_case_with_question_id_dto
    ):
    # Arrange
    question_id = 1
    test_case_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = CreateTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    problem_statement_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = True
    test_case_storage.is_test_case_belongs_to_question.return_value = True
    test_case_storage.create_test_case.return_value = \
        test_case_with_question_id_dto
    presenter.get_create_test_case_response.return_value = \
        test_case_with_question_id_dict

    # Act
    response = interactor.create_test_case(
        question_id=question_id,
        test_case_details=test_case_dict
    )

    # Assert
    assert response == test_case_with_question_id_dict
    problem_statement_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.update_test_case.assert_called_once_with(
        test_case_details=test_case_dto
    )
