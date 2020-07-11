from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


def test_raise_invalid_question_id_exception_raises_error():
    # Arrange
    import json
    presenter = PresenterImplementation()
    expected_error = {
        "response": "Question id is not valid.",
        "http_status_code": 404,
        "res_status":  "INVALID_QUESTION_ID"
    }

    # Act
    error = presenter.raise_invalid_question_id_exception()

    # Arrange
    assert json.loads(error.content) == expected_error
