import pytest
from content_management_portal_auth.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound


def test_raise_invalid_username_exception_raises_error():
    # Arrange
    presenter = PresenterImplementation()

    with pytest.raises(NotFound):
        presenter.raise_invalid_username_exception()
