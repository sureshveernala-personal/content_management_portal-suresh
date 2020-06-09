from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.interactors.get_questions_interactor \
    import GetQuestionsInteractor
from content_management_portal.interactors.storages.dtos import\
    QuestionStatusDto, QuestionsDto


def test_get_questions_interactor_with_invalid_offset_value():
    # Arrange
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        problem_statement_storage=problem_statement_storage,
        presenter=presenter
    )
    offset = 0
    limit = 1

    presenter.raise_invalid_offset_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_questions(offset=offset, limit=limit)

    # Assert
    problem_statement_storage.get_questions.assert_not_called()
    presenter.get_questions_response.assert_not_called()

def test_get_questions_interactor_with_invalid_limit_value():
    # Arrange
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        problem_statement_storage=problem_statement_storage,
        presenter=presenter
    )
    offset = 1
    limit = 0

    presenter.raise_invalid_limit_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_questions(offset=offset, limit=limit)

    # Assert
    problem_statement_storage.get_questions.assert_not_called()
    presenter.get_questions_response.assert_not_called()


def test_get_questions_interactor():
    # Arrange
    problem_statement_storage = create_autospec(
        ProblemStatementStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionsInteractor(
        problem_statement_storage=problem_statement_storage,
        presenter=presenter
    )
    offset = 1
    limit = 1
    question_status_dto = QuestionStatusDto(
        question_id=1,
        statement="string",
        rough_solution_status=True,
        test_cases_status=True,
        prefilled_code_status=True,
        solution_approach_status=True,
        clean_solution_status=True,
        hint_status=True
    )

    questions_dto = QuestionsDto(
        total_questions=1,
        offset=1,
        limit=1,
        questions_list=[question_status_dto]
    )
    expected_dict = {
        "total_questions": 1,
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
                "clean_solution_status": True,
                "hint_status": True
            }
        ]
    }

    problem_statement_storage.get_questions.return_value = questions_dto
    presenter.get_questions_response.return_value = expected_dict

    # Act
    questions_dict = interactor.get_questions(offset=offset, limit=limit)

    # Assert
    problem_statement_storage.get_questions.assert_called_once()
    presenter.get_questions_response.assert_called_once_with(questions_dto)
    assert questions_dict == expected_dict
