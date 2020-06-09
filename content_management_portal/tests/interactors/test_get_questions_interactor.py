from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.interactors.get_questions_interactor \
    import GetQuestionsInteractor
from content_management_portal.interactors.storages.dtos import\
    QuestionStatusDto


def test_get_questions_interactor_with_invalid_offset_value():
    # Arrange
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    offset = 0
    limit = 1
    total_questions = 10
    question_storage.get_total_number_of_questions.return_value = total_questions
    presenter.raise_invalid_offset_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_questions(offset=offset, limit=limit)

    # Assert
    question_storage.get_questions.assert_not_called()
    presenter.get_questions_response.assert_not_called()

def test_get_questions_interactor_with_invalid_limit_value():
    # Arrange
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    offset = 1
    limit = 0
    total_questions = 10
    question_storage.get_total_number_of_questions.return_value = total_questions
    presenter.raise_invalid_limit_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_questions(offset=offset, limit=limit)

    # Assert
    question_storage.get_questions.assert_not_called()
    presenter.get_questions_response.assert_not_called()


def test_get_questions_interactor():
    # Arrange
    offset = 1
    limit = 1
    total_questions = 10
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    question_storage.get_total_number_of_questions.return_value = total_questions
    question_status_dtos = [
        QuestionStatusDto(
            question_id=10,
            statement="string",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True
        )
    ]

    expected_dict = {
        "total_questions": total_questions,
        "offset": 1,
        "limit": 1,
        "questions_list": [
            {
                "question_id": 1,
                "statement": "string",
                "rough_solution_status": True,
                "test_cases_status": True,
                "prefilled_code_status": True,
                "solution_approach_status": True,
                "clean_solution_status": True
            }
        ]
    }

    question_storage.get_questions.return_value = question_status_dtos
    presenter.get_questions_response.return_value = expected_dict

    # Act
    questions_dict = interactor.get_questions(offset=offset, limit=limit)

    # Assert
    question_storage.get_questions.assert_called_once_with(
        from_value=0, to_value=1
    )
    presenter.get_questions_response.assert_called_once_with(
        offset=limit, limit=limit, total_questions=total_questions, question_status_dtos=question_status_dtos)
    assert questions_dict == expected_dict


def test_get_questions_interactor_when_offset_greater_then_total_number_of_questions():
    # Arrange
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    total_questions = 1
    question_storage.get_total_number_of_questions.return_value = total_questions
    offset = 2
    limit = 1
    question_status_dtos = []

    expected_dict = {
        "total_questions": total_questions,
        "offset": 2,
        "limit": 1,
        "questions_list": []
    }

    question_storage.get_questions.return_value = question_status_dtos
    presenter.get_questions_response.return_value = expected_dict

    # Act
    questions_dict = interactor.get_questions(offset=offset, limit=limit)

    # Assert
    question_storage.get_questions.assert_called_once_with(
        from_value=0, to_value=0
    )
    presenter.get_questions_response.assert_called_once_with(
        offset=2, limit=1, question_status_dtos=question_status_dtos,
        total_questions=total_questions
    )
    assert questions_dict == expected_dict
