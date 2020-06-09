from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.interactors.get_question_details_interactor \
    import GetQuestionDetailsInteractor


def test_get_question_details_interactor_with_invalid_question_id():
    # Arrange
    question_id = 1
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionDetailsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    question_storage.is_valid_question_id.return_value = False
    presenter.raise_invalid_question_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_question_details(question_id=question_id)

    # Assert
    question_storage.get_question_details.assert_not_called()


def test_get_question_details_interactor_with_valid_details(
        statement_dict, rough_solution_dicts_with_ids,
        clean_solution_dicts_with_ids, test_case_dict, solution_approach_dict,
        hint_dict, prefilled_code_dicts_with_ids, question_dto,
        rough_solution_dtos_with_ids, clean_solution_dtos_with_ids,
        test_case_dto, solution_approach_dto, hint_dto,
        prefilled_code_dtos_with_ids
    ):
    # Arrange
    question_id = 1
    question_storage = create_autospec(
        QuestionStorageInterface
    )
    presenter = create_autospec(PresenterInterface)
    interactor = GetQuestionDetailsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )
    expected_dict = {
        "question_id": 1,
        "statement": statement_dict,
        "rough_solutions": rough_solution_dicts_with_ids,
        "clean_solutions": clean_solution_dicts_with_ids,
        "prefilled_codes": prefilled_code_dicts_with_ids,
        "test_cases": [test_case_dict],
        "hints": [hint_dict],
        "solution_approach": solution_approach_dict
    }

    question_storage.get_question_details.return_value = \
        question_dto, rough_solution_dtos_with_ids,\
        clean_solution_dtos_with_ids, [test_case_dto],\
        solution_approach_dto, [hint_dto],\
        prefilled_code_dtos_with_ids
    presenter.get_question_details_response.return_value = expected_dict

    # Act
    response = interactor.get_question_details(
        question_id=question_id
    )

    # Assert
    question_storage.get_question_details.assert_called_once_with(
        question_id=question_id
    )
    presenter.get_question_details_response.assert_called_once_with(
        question_dto=question_dto,
        rough_solution_dtos=rough_solution_dtos_with_ids,
        clean_solution_dtos=clean_solution_dtos_with_ids,
        test_case_dtos=[test_case_dto],
        solution_approach_dto=solution_approach_dto,
        hint_dtos=[hint_dto],
        prefilled_code_dtos=prefilled_code_dtos_with_ids
    )
    assert response == expected_dict
