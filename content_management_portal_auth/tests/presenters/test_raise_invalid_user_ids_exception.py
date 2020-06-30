import pytest
from content_management_portal_auth.presenters.presenter_implementation import\
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal_auth.exceptions.exceptions import InvalidUserIds


def test_raise_invalid_user_ids_exception_raises_error():
    # Arrange
    user_ids = [1, 2]
    error = InvalidUserIds(user_ids=user_ids)
    presenter = PresenterImplementation()

    with pytest.raises(NotFound):
        presenter.raise_invalid_user_ids_exception(error=error)
