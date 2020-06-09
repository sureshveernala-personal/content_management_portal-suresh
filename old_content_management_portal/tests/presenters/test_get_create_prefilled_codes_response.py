import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.storages.dtos import \
    PrefilledCodesWithQuestionIdDto


def test_get_create_prefilled_codes_response_when_no_prefilled_codes_returns_empty_list():
    # Arrange
    presenter = PresenterImplementation()
    prefilled_code_dtos = PrefilledCodesWithQuestionIdDto(
        question_id=1,prefilled_codes=[]
    )
    excepted_response = {
        "question_id":1,
        "prefilled_codes": []
    }

    # Act
    response = presenter.get_create_prefilled_codes_response(
        prefilled_codes_dto_with_question_id\
        =prefilled_code_dtos
    )

    # Assert
    assert response == excepted_response


def test_get_create_prefilled_codes_response_when_prefilled_codes_given_returns_list_of_prefilled_codes(
        prefilled_code_with_question_id_dicts, prefilled_code_with_question_id_dtos
    ):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_prefilled_codes_response(
        prefilled_codes_dto_with_question_id=\
        prefilled_code_with_question_id_dtos
    )

    # Assert
    assert response == prefilled_code_with_question_id_dicts
