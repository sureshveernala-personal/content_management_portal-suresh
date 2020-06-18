from abc import ABC, abstractmethod
from typing import List
from gyaan.interactors.storages.dtos import DomainDto, DomainStatsDto,\
    UserDto, JoiningRequestDto, PostDto, PostTagDto, PostReactionsCountDto,\
    CommentsCountDto, CommentDto, CommentReactionsCountDto, RepliesCountDto

@abstractmethod
class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass


    @abstractmethod
    def validate_does_user_domain_member(self, user_id:int, domain_id: int):
        pass


    @abstractmethod
    def get_domain(self, domain_id: int) -> DomainDto:
        pass


    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> List[DomainStatsDto]:
        pass


    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass


    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDto]:
        pass


    @abstractmethod
    def get_domain_joining_requests(self, domain_id: int) \
        -> List[JoiningRequestDto]:
        pass


    @abstractmethod
    def get_total_post_ids(self):
        pass


    @abstractmethod
    def get_posts(self, post_ids: List[int]) -> List[PostDto]:
        pass


    @abstractmethod
    def get_post_tags(self, post_ids: List[int]) -> List[PostTagDto]:
        pass


    @abstractmethod
    def get_post_reactions_count(
            self, post_ids: List[int]
        ) -> PostReactionsCountDto:
        pass


    @abstractmethod
    def get_comments_count(
            self, post_ids: List[int]
        ) -> List[CommentsCountDto]:
        pass


    @abstractmethod
    def get_latest_comments(
            self, post_id: int, limit: int
        ) -> List[CommentDto]:
        pass


    @abstractmethod
    def get_comment_reactions_count(
            self, comment_ids: List[int]
        ) -> CommentReactionsCountDto:
        pass


    @abstractmethod
    def get_replies_count(
            self, comment_ids: List[int]
        ) -> List[RepliesCountDto]:
        pass


    @abstractmethod
    def get_domain_post_ids(
            self,domain_id: int, offset: int, limit: int
        ) -> List[int]:
        pass


    @abstractmethod
    def get_total_doamain_posts_count(self, domain_id: int) -> int:
        pass
