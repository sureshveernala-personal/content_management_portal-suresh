from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.exceptions.exceptions import InvalidDomainId, UserNotDomainMember,\
    InvalidOffsetValue, InvalidLimitValue
from gyaan.interactors.get_domain_posts_interactor import \
    GetDomainPostsInteractor
from gyaan.interactors.get_domain_details_interactor import \
    GetDomainDetailsInteractor
from gyaan.interactors.presenters.dtos import DomainDetailsWithPostsDto


class GetDomainWithPostsInteractor():

    def __init__(self,  storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(
            self, user_id: int, domain_id:  int, offset: int, limit:int,
            presenter: PresenterInterface
        ):
        try:
            response = self._prepare_get_domain_with_posts_response(
                user_id=user_id, domain_id=domain_id, offset=offset,
                limit=limit, presenter=presenter
            )
            return response
        except InvalidDomainId:
            presenter.raise_invalid_domain_id_exception()
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()
        except InvalidOffsetValue:
            presenter.raise_invalid_offset_value_exception()
        except InvalidLimitValue:
            presenter.raise_invalid_limit_value_exception()


    def _prepare_get_domain_with_posts_response(
            self, user_id: int, domain_id:  int, offset: int, limit:int,
            presenter: PresenterInterface
        ):
        domain_details_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit
        )
        response = presenter.get_domain_with_posts_response(
            domain_details_with_posts_dto=domain_details_with_posts_dto
        )
        return response


    def get_domain_with_posts(
            self, user_id: int, domain_id:  int, offset: int, limit:int
        ):

        get_domain_details_interactor= \
            GetDomainDetailsInteractor(storage=self.storage)
        domain_details_dto = get_domain_details_interactor.get_domain_details(
            user_id=user_id, domain_id=domain_id
        )

        get_domain_posts_interactor = \
            GetDomainPostsInteractor(storage=self.storage)
        post_details_dto = get_domain_posts_interactor.get_domain_posts(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit
        )

        domain_details_with_posts_dto = DomainDetailsWithPostsDto(
            post_details_dto=post_details_dto,
            domain_details_dto=domain_details_dto
        )
        return domain_details_with_posts_dto


    def validate_offset(self, offset: int):
        is_negative = offset < 0
        if is_negative:
            raise InvalidOffsetValue


    def validate_limit(self, limit: int):
        is_negative = limit < 0
        if is_negative:
            raise InvalidLimitValue
