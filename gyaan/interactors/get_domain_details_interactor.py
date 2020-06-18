from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.exceptions.exceptions import InvalidDomainId, UserNotDomainMember
from gyaan.interactors.presenters.dtos import DomainDetailsDTO


class GetDomainDetailsInteractor():
    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_domain_details_wrapper(
            self, user_id: int, domain_id: int, presenter: PresenterInterface
        ):
        try:
            response = self._get_domain_details_response(
                user_id=user_id,domain_id=domain_id, presenter=presenter
            )
            return response
        except InvalidDomainId:
            presenter.raise_invalid_domain_id_exception()
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()


    def _get_domain_details_response(
            self, presenter: PresenterInterface, user_id:int, domain_id: int
        ):
        domain_details_dto = self.get_domain_details(
            user_id=user_id, domain_id=domain_id
        )
        response = presenter.get_domain_details_response(
            domain_details_dto=domain_details_dto
        )
        return response

    def get_domain_details(self, user_id: int, domain_id: int):
        self.storage.validate_domain_id(domain_id=domain_id)
        self.storage.validate_does_user_domain_member(
            user_id=user_id, domain_id=domain_id
        )
        domain_dto, domain_stats_dto, expert_user_dtos,\
        domain_join_request_dtos, domain_join_requested_user_dtos,\
        is_user_domain_expert = self._dtos_required_for_domain_details(
            domain_id=domain_id, user_id=user_id
        )
        demain_details_dto = DomainDetailsDTO(
            domain_id=domain_id,
            domain_dto=domain_dto,
            user_id=user_id,
            domain_stats=domain_stats_dto,
            expert_users=expert_user_dtos,
            is_user_domain_expert=is_user_domain_expert,
            domain_join_requests=domain_join_request_dtos,
            joining_requested_users=domain_join_requested_user_dtos
        )
        return demain_details_dto


    def _dtos_required_for_domain_details(self, domain_id: int, user_id: int):
        domain_dto = self.storage.get_domain(domain_id=domain_id)
        domain_stats_dto = self.storage.get_domain_stats(domain_id=domain_id)
        expert_user_ids = self.storage.get_domain_expert_ids(
            domain_id=domain_id
        )
        expert_user_dtos = self.storage.get_users_details(
            user_ids=expert_user_ids
        )
        is_user_domain_expert = user_id in expert_user_ids
        domain_join_request_dtos = []
        if is_user_domain_expert:
            domain_join_request_dtos = self.storage.get_domain_joining_requests(
                domain_id=domain_id
            )
        domain_join_requested_user_ids = [
            join_request.user_id
            for join_request in domain_join_request_dtos
        ]
        domain_join_requested_user_dtos = self.storage.get_users_details(
            user_ids=domain_join_requested_user_ids
        )
        return (
            domain_dto, domain_stats_dto, expert_user_dtos,
            domain_join_request_dtos, domain_join_requested_user_dtos,
            is_user_domain_expert
        )
