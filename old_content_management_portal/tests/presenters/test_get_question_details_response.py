from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
import pytest


@pytest.mark.django_db
def test_get_question_details_response(
        statement_dict, rough_solution_dicts,
        clean_solution_dicts, test_case_dict, solution_approach_dict,
        hint_dict, prefilled_code_dicts, question_dto,
        rough_solution_dtos, clean_solution_dtos,
        test_case_dto, solution_approach_dto, hint_dto,
        prefilled_code_dtos
    ):
    # Arrange
    storage = PresenterImplementation()
    expected_dict = {
        "question_id": 1,
        "statement": statement_dict,
        "rough_solutions": rough_solution_dicts,
        "clean_solutions": clean_solution_dicts,
        "prefilled_codes": prefilled_code_dicts,
        "test_cases": [test_case_dict],
        "hints": [hint_dict],
        "solution_approach": solution_approach_dict
    }


    # Act
    question_details_dict = storage.get_question_details_response(
        question_dto=question_dto,
        rough_solution_dtos=rough_solution_dtos,
        clean_solution_dtos=clean_solution_dtos,
        test_case_dtos=[test_case_dto],
        solution_approach_dto=solution_approach_dto,
        hint_dtos=[hint_dto],
        prefilled_code_dtos=prefilled_code_dtos
    )

    # Assert
    assert expected_dict == question_details_dict


@pytest.mark.django_db
def test_get_question_details_response_when_no_sub_categeries_available(
        statement_dict, question_dto
    ):
    # Arrange
    storage = PresenterImplementation()
    expected_dict = {
        "question_id": 1,
        "statement": statement_dict,
        "rough_solutions": [],
        "clean_solutions": [],
        "prefilled_codes": [],
        "test_cases": [],
        "hints": [],
        "solution_approach": None
    }


    # Act
    question_details_dict = storage.get_question_details_response(
        question_dto=question_dto,
        rough_solution_dtos=[],
        clean_solution_dtos=[],
        test_case_dtos=[],
        solution_approach_dto=None,
        hint_dtos=[],
        prefilled_code_dtos=[]
    )

    # Assert
    assert question_details_dict == expected_dict
