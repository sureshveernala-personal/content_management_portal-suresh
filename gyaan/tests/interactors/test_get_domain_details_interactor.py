from unittest.mock import create_autospec
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.get_domain_details_interactor import \
    GetDomainDetailsInteractor
from gyaan.exceptions.exceptions import InvalidDomainId, UserNotDomainMember


def test_get_domain_details_with_invalid_domain_id():
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    storage.validate_domain_id.side_effect = InvalidDomainId
    presenter.raise_invalid_domain_id_exception.side_effect = NotFound

    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            user_id=user_id, domain_id=domain_id, presenter=presenter
        )


def test_get_domain_details_when_user_not_a_domain_member():
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    storage.validate_does_user_domain_member.side_effect = UserNotDomainMember
    presenter.raise_user_not_domain_member_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_domain_details_wrapper(
            user_id=user_id, domain_id=domain_id, presenter=presenter
        )


def test_get_domain_details_when_user_was_expert(
        domain_dto, user_dtos, joining_requested_users, domain_stats_dtos,
        domain_details_dto, joining_request_dtos
    ):
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    storage.get_domain.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats_dtos
    storage.get_domain_expert_ids.return_value = [1, 2]
    storage.get_users_details.side_effect = [
        user_dtos, joining_requested_users
    ]
    storage.get_domain_joining_requests.return_value = joining_request_dtos
    presenter.get_domain_details_response.return_value = "domain_details_dict"

    # Act
    response = interactor.get_domain_details_wrapper(
            user_id=user_id, domain_id=domain_id, presenter=presenter
        )

    # Assert
    storage.get_domain.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_domain_joining_requests.assert_called_once_with(
        domain_id=domain_id
    )

    first_time_argument = storage.get_users_details.call_args_list[0].kwargs
    assert first_time_argument['user_ids'] == [1, 2]
    second_time_argument = storage.get_users_details.call_args_list[1].kwargs
    assert second_time_argument['user_ids'] == [3, 4]
    presenter.get_domain_details_response.assert_called_once_with(
        domain_details_dto=domain_details_dto
    )
    assert response == "domain_details_dict"


def test_get_domain_details_when_user_was_not_expert(
        domain_dto, user_dtos, joining_requested_users, domain_stats_dtos,
        domain_details_dto_when_user_not_expert, joining_request_dtos
    ):
    # Arrange
    domain_id = 1
    user_id = 2
    storage = create_autospec(StorageInterface)
    presenter =create_autospec(PresenterInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    storage.get_domain.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats_dtos
    storage.get_domain_expert_ids.return_value = [1]
    storage.get_users_details.side_effect = [
        user_dtos[:1], []
    ]
    storage.get_domain_joining_requests.return_value = joining_request_dtos
    presenter.get_domain_details_response.return_value = "domain_details_dict"


    # Act
    response = interactor.get_domain_details_wrapper(
            user_id=user_id, domain_id=domain_id, presenter=presenter
        )

    # Assert
    storage.get_domain.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_domain_joining_requests.assert_not_called()
    first_time_argument = storage.get_users_details.call_args_list[0].kwargs
    assert first_time_argument['user_ids'] == [1]
    second_time_argument = storage.get_users_details.call_args_list[1].kwargs
    assert second_time_argument['user_ids'] == []
    presenter.get_domain_details_response.assert_called_once_with(
        domain_details_dto=domain_details_dto_when_user_not_expert
    )
    assert response == "domain_details_dict"
