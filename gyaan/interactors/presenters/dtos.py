from dataclasses import dataclass
from typing import List
from gyaan.interactors.storages.dtos import DomainDto, DomainStatsDto,\
    UserDto, JoiningRequestDto, PostDto, PostTagDto, PostReactionsCountDto,\
    CommentsCountDto, CommentDto, CommentReactionsCountDto, RepliesCountDto



@dataclass
class DomainDetailsDTO:
    domain_id: int
    domain_dto: DomainDto
    user_id: int
    domain_stats: List[DomainStatsDto]
    expert_users: List[UserDto]
    is_user_domain_expert: bool
    domain_join_requests: List[JoiningRequestDto]
    joining_requested_users: List[UserDto]


@dataclass
class PostDetailsDto:
    post_dtos: List[PostDto]
    post_tags: List[PostTagDto]
    post_reaction_counts: List[PostReactionsCountDto]
    comments_counts: List[CommentsCountDto]
    comment_dtos: List[CommentDto]
    comment_reactions_counts: List[CommentReactionsCountDto]
    replies_counts: List[RepliesCountDto]
    user_dtos: List[UserDto]


@dataclass
class DomainDetailsWithPostsDto:
    domain_details_dto: DomainDetailsDTO
    post_details_dto: PostDetailsDto