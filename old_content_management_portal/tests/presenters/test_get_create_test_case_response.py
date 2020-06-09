import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


def test_get_create_test_case_response_returns_dict(
        test_case_with_question_id_dto, test_case_with_question_id_dict
    ):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_test_case_response(
        test_case_with_question_id_dto=test_case_with_question_id_dto
    )

    # Assert
    assert response == test_case_with_question_id_dict
