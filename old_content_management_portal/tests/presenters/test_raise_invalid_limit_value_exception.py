import pytest
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_raise_invalid_limit_value_exception_raises_error():
    # Arrange
    presenter = PresenterImplementation()

    with pytest.raises(BadRequest):
        presenter.raise_invalid_limit_value_exception()
