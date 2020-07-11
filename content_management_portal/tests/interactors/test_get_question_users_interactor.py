from unittest.mock import create_autospec, patch
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.interactors.get_question_user_interactor \
    import GetQuestionUserInteractor
from content_management_portal.interactors.storages.dtos import UserDto
from content_management_portal.tests.common_fixtures.adapters import auth_service

def test_get_question_user_interactor_with_invalid_question_id():
    # Arrange
    question_id = 1
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionUserInteractor(
        question_storage=question_storage
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    with pytest.raises(NotFound):
        interactor.get_question_user_wrapper(
            question_id=question_id, presenter=presenter
        )


# @patch('content_management_portal.adapters.user_service.UserService')
def test_get_question_user_interactor_with_valid_details(mocker):
    # Arrange
    question_id = 1
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionUserInteractor(
        question_storage=question_storage
    )
    expected_dicts = [
        {
            "username": "suresh",
            "user_id": 1
        }
    ]
    expected_dto = [
        UserDto(
            username="suresh",
            user_id=1
        )
    ]
    auth_service.prepare_get_user_dtos_mock(mocker, user_ids=[1])
    question_storage.is_valid_question_id.return_value = True
    question_storage.get_question_user_id.return_value = [1]
    presenter.get_question_user_response.return_value = expected_dicts
    # user_service.get_user_dtos.return_value = expected_dto

    # Act
    user_dicts = interactor.get_question_user_wrapper(
        question_id=question_id, presenter=presenter
    )

    # Assert
    assert user_dicts == expected_dicts
