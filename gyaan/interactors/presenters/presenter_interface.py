from abc import ABC
from abc import abstractmethod
from gyaan.interactors.presenters.dtos import DomainDetailsDTO,\
    PostDetailsDto, DomainDetailsWithPostsDto
from gyaan.exceptions.exceptions import InvalidPostIds


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass


    @abstractmethod
    def raise_user_not_domain_member_exception(self):
        pass

    @abstractmethod
    def get_domain_details_response(
            self, domain_details_dto: DomainDetailsDTO
        ):
        pass

    @abstractmethod
    def raise_invalid_post_ids_exception(self, error: InvalidPostIds):
        pass


    @abstractmethod
    def get_posts_response(self, post_details_dto: PostDetailsDto):
        pass


    @abstractmethod
    def get_domain_posts_response(self, post_details_dto: PostDetailsDto):
        pass


    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass


    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass


    @abstractmethod
    def get_domain_with_posts_response(
            self, domain_details_with_posts_dto: DomainDetailsWithPostsDto
        ):
        pass
