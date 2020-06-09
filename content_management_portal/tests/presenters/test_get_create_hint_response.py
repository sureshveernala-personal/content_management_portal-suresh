import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


def test_get_create_hint_response_returns_dict(
        hint_with_question_id_dto, hint_with_question_id_dict
    ):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_hint_response(
        question_id=1,
        hint_with_question_id_dto=hint_with_question_id_dto
    )

    # Assert
    assert response == hint_with_question_id_dict
