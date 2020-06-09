from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.constants.enums import \
    DescriptionType, CodeLanguage
from content_management_portal.models import Question
import pytest


@pytest.mark.django_db
def test_get_question_details_returns_question_details_dto(
        rough_solution, clean_solution, prefilled_code, test_case, hint,
        solution_approach, question_dto, rough_solution_dtos,
        clean_solution_dtos, prefilled_code_dtos,
        test_case_dtos, solution_approach_dto, hint_dtos
    ):
    # Arrange
    question_id = 1
    rough_solution_dtos = rough_solution_dtos[:1]
    clean_solution_dtos = clean_solution_dtos[:1]
    prefilled_code_dtos = prefilled_code_dtos[:1]
    storage = QuestionStorageImplementation()

    # Act
    response_question_dto, response_rough_solution_dtos,\
    response_clean_solution_dtos, response_test_case_dtos,\
    response_solution_aproach, response_hints,\
    response_prefilled_code_dtos = \
        storage.get_question_details(question_id=question_id)

    # Assert
    assert response_question_dto == question_dto
    assert response_rough_solution_dtos == rough_solution_dtos
    assert response_clean_solution_dtos == clean_solution_dtos
    assert response_solution_aproach == solution_approach_dto
    assert response_prefilled_code_dtos == prefilled_code_dtos
    assert response_test_case_dtos == test_case_dtos
    assert response_hints == hint_dtos

@pytest.mark.django_db
def test_get_question_details_when_no_data(
        question, question_dto):
    # Arrange
    question_id = 1
    storage = QuestionStorageImplementation()

    # Act
    response_question_dto, response_rough_solution_dtos,\
    response_clean_solution_dtos, response_test_case_dtos,\
    response_solution_aproach, response_hints,\
    response_prefilled_code_dtos = \
        storage.get_question_details(question_id=question_id)

    # Assert
    assert response_question_dto == question_dto
    assert response_rough_solution_dtos == []
    assert response_clean_solution_dtos == []
    assert response_solution_aproach == None
    assert response_prefilled_code_dtos == []
    assert response_test_case_dtos == []
    assert response_hints == []
