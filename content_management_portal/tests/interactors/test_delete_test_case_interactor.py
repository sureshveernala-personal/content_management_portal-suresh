import pytest
from unittest.mock import create_autospec
from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.delete_test_case_interactor\
    import DeleteTestCaseInteractor
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_delete_test_case_interactor_with_invalid_question_id_raises_error():
    # Arrange
    test_case_id = 1
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    test_case_storage.is_valid_test_case_id.return_value = True
    test_case_storage.\
        is_test_case_belongs_to_question.return_value = True
    presenter.raise_invalid_question_id_exception.side_effect = NotFound
    test_case_storage.delete_test_case.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_test_case(
            test_case_id=test_case_id, question_id=question_id
        )

    # Assert
    question_storage.is_valid_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.delete_test_case.assert_not_called()


def test_delete_test_case_interactor_with_invalid_test_case_id_raises_error():
    # Arrange
    test_case_id = 1
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = False
    test_case_storage.\
        is_test_case_belongs_to_question.return_value = True
    presenter.raise_invalid_test_case_id_exception.side_effect = NotFound
    test_case_storage.delete_test_case.return_value = None

    # Act
    with pytest.raises(NotFound):
        interactor.delete_test_case(
            test_case_id=test_case_id, question_id=question_id
        )

    # Assert
    test_case_storage.is_valid_test_case_id.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.delete_test_case.assert_not_called()


def test_delete_test_case_interactor_with_test_case_not_belong_to_question_raises_error():
    # Arrange
    test_case_id = 1
    question_id = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = True
    test_case_storage.\
        is_test_case_belongs_to_question.return_value = False
    presenter.raise_test_case_not_belongs_to_question_exception.side_effect = \
        BadRequest
    test_case_storage.delete_test_case.return_value = None

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_test_case(
            test_case_id=test_case_id, question_id=question_id
        )

    # Assert
    test_case_storage.is_valid_test_case_id.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.delete_test_case.assert_not_called()


def test_delete_test_case_interactor_with_valid_details():
    # Arrange
    test_case_id = 1
    question_id = 1
    test_case_number = 1
    test_case_storage = create_autospec(TestCaseStorageInterface)
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteTestCaseInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = True
    test_case_storage.is_valid_test_case_id.return_value = True
    test_case_storage.\
        is_test_case_belongs_to_question.return_value = True
    test_case_storage.delete_test_case.return_value = test_case_number

    # Act
    interactor.delete_test_case(
        test_case_id=test_case_id,
        question_id=question_id
    )

    # Assert
    test_case_storage.is_valid_test_case_id.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.delete_test_case.assert_called_once_with(
        test_case_id=test_case_id, question_id=question_id
    )
    test_case_storage.\
        decrease_test_case_numbers_followed_given_test_case_number.\
            assert_called_once_with(
                question_id=1, test_case_number=test_case_number
            )
