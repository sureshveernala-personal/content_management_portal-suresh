from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.exceptions.exceptions import InvalidDomainId, UserNotDomainMember,\
    InvalidOffsetValue, InvalidLimitValue
from gyaan.interactors.get_posts_interactor import GetPostsInteractor


class GetDomainPostsInteractor():

    def __init__(self,  storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_wrapper(
            self, user_id: int, domain_id:  int, offset: int, limit:int,
            presenter: PresenterInterface
        ):
        try:
            response = self._prepare_get_domain_posts_response(
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


    def _prepare_get_domain_posts_response(
            self, user_id: int, domain_id:  int, offset: int, limit:int,
            presenter: PresenterInterface
        ):
        post_details_dto = self.get_domain_posts(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit
        )
        response = presenter.get_domain_posts_response(
            post_details_dto=post_details_dto
        )
        return response


    def get_domain_posts(
            self, user_id: int, domain_id:  int, offset: int, limit:int
        ):
        self.storage.validate_domain_id(domain_id=domain_id)

        self.storage.validate_does_user_domain_member(
            user_id=user_id, domain_id=domain_id
        )
        self.validate_offset(offset=offset)
        self.validate_limit(limit=limit)

        domain_posts_count = \
            self.storage.get_total_doamain_posts_count(domain_id=domain_id)
        is_offset_more_available = offset > domain_posts_count
        if is_offset_more_available:
            return []

        domain_post_ids = self.storage.get_domain_post_ids(
            domain_id=domain_id, offset=offset, limit=limit
        )

        interactor = GetPostsInteractor(storage=self.storage)

        post_details_dto = interactor.get_posts(post_ids=domain_post_ids)
        return post_details_dto
    
    
    def validate_offset(self, offset: int):
        is_negative = offset < 0
        if is_negative:
            raise InvalidOffsetValue
    
    
    def validate_limit(self, limit: int):
        is_negative = limit < 0
        if is_negative:
            raise InvalidLimitValue
