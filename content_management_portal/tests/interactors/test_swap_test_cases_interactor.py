from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.swap_test_cases_interactor\
    import SwapTestCasesInteractor


def test_create_test_case_interactor_with_invalid_question_id_raises_error(
        test_cases_swap_details_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_test_cases(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_not_called()


def test_create_test_case_interactor_with_invalid_first_test_case_id_raises_error(
        test_cases_swap_details_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.get_test_case_ids.return_value = [2]
    test_case_storage.get_given_question_test_case_ids.return_value = [1, 2]
    presenter.raise_invalid_test_case_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_test_cases(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_not_called()

def test_create_test_case_interactor_with_invalid_second_test_case_id_raises_error(
        test_cases_swap_details_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.get_test_case_ids.return_value = [1]
    test_case_storage.get_given_question_test_case_ids.return_value = [1, 2]
    presenter.raise_invalid_test_case_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.swap_test_cases(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_not_called()

def test_create_test_case_interactor_when_first_test_case_id_not_belongs_to_raises_error(
        test_cases_swap_details_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.get_test_case_ids.return_value = [1, 2]
    test_case_storage.get_given_question_test_case_ids.return_value = [2]
    presenter.raise_test_case_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.swap_test_cases(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_not_called()


def test_create_test_case_interactor_when_second_test_case_id_not_belongs_to_raises_error(
        test_cases_swap_details_dict
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.get_test_case_ids.return_value = [1, 2]
    test_case_storage.get_given_question_test_case_ids.return_value = [1]
    presenter.raise_test_case_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.swap_test_cases(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details_dict
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_not_called()


def test_create_test_case_interactor_with_with_valid_details(
        test_cases_swap_details_dict, test_cases_swap_details_dto
    ):
    # Arrange
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.get_test_case_ids.return_value = [1, 2]
    test_case_storage.get_given_question_test_case_ids.return_value = [1, 2]
    presenter.raise_test_case_not_belongs_to_question_exception.side_effect = \
        BadRequest

    # Act
    interactor.swap_test_cases(
        question_id=question_id,
        test_cases_swap_details=test_cases_swap_details_dict
    )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.swap_test_cases.assert_called_with(
        test_cases_swap_details=test_cases_swap_details_dto
    )
