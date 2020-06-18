from unittest.mock import create_autospec, patch
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.get_domain_with_posts_interactor import \
    GetDomainWithPostsInteractor
from gyaan.exceptions.exceptions import InvalidDomainId, UserNotDomainMember
from gyaan.interactors.get_posts_interactor import GetPostsInteractor


def test_get_domain_with_posts_with_invalid_domain_id_raises_error():
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 5
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    storage.validate_domain_id.side_effect = InvalidDomainId
    presenter.raise_invalid_domain_id_exception.side_effect = NotFound

    with pytest.raises(NotFound):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )


def test_get_domain_with_posts_when_user_not_a_domain_member_raises_error():
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 5
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    storage.validate_does_user_domain_member.side_effect = UserNotDomainMember
    presenter.raise_user_not_domain_member_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )


def test_get_domain_with_posts_with_invalid_offset_value_member_raises_error():
    # Arrange
    domain_id = 1
    user_id = 1
    offset = -1
    limit = 5
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter.raise_invalid_offset_value_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )


def test_get_domain_with_posts_with_invalid_limit_value_member_raises_error():
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 1
    limit = -1
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter.raise_invalid_limit_value_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )


def test_get_domain_with_posts_when_offset_more_then_available():
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 2
    limit = 5
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    storage.get_total_doamain_posts_count.return_value = 1
    presenter.get_domain_with_posts_response.return_value = "get_domain_with_posts"

    # Act
    response = interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )

    # Assert
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_details_with_posts_dto=[]
    )
    assert response == "get_domain_with_posts"



@patch('gyaan.interactors.get_domain_details_interactor\
.GetDomainDetailsInteractor.get_domain_details')
@patch('gyaan.interactors.get_domain_posts_interactor.\
GetDomainPostsInteractor.get_domain_posts')
def test_get_domain_with_posts_with_valid_details(
        get_domain_posts_mock, get_domain_details_mock,
        domain_details_with_posts_dto, post_details_dto, domain_details_dto
    ):
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 5
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    get_domain_posts_mock.return_value = post_details_dto
    get_domain_details_mock.return_value = domain_details_dto
    storage.get_total_doamain_posts_count.return_value = 10
    presenter.get_domain_with_posts_response.return_value = "get_domain_with_posts"

    # Act
    response = interactor.get_domain_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter
        )

    # Assert
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_details_with_posts_dto=domain_details_with_posts_dto
    )
    assert response == "get_domain_with_posts"
