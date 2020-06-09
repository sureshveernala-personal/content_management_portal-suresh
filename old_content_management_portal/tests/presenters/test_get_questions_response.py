import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.dtos import\
    QuestionStatusDto, QuestionsDto


def test_get_questions_response():
    # Arrange
    presenter = PresenterImplementation()
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

    # Act
    response = presenter.get_questions_response(questions_dto=questions_dto)

    # Assert
    assert response == expected_dict
