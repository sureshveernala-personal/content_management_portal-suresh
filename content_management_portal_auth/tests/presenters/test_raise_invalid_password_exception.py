import pytest
from content_management_portal_auth.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import Forbidden


def test_raise_invalid_password_exception_raises_error():
    # Arrange
    presenter = PresenterImplementation()

    with pytest.raises(Forbidden):
        presenter.raise_invalid_password_exception()
