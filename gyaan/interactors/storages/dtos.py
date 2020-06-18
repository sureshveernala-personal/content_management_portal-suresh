from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDto:
    user_id: int
    user_name: str
    profile_pic: str


@dataclass
class DomainDto:
    domain_id: int
    title: str
    description: str


@dataclass
class DomainStatsDto:
    domain_id: int
    posts_count: int
    members_count: int
    bookmark_count: int


@dataclass
class JoiningRequestDto:
    joining_request_id: int
    user_id: int


@dataclass
class PostDto:
    post_id: int
    title: str
    content: str
    posted_at: datetime
    posted_by_id: int


@dataclass
class PostTagDto:
    post_id: int
    tag_id: int
    name: str


@dataclass
class PostReactionsCountDto:
    post_id: int
    reactions_count: int


@dataclass
class CommentsCountDto:
    comment_id: int
    comments_count: int


@dataclass
class CommentDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by_id: int
    post_id: int


@dataclass
class CommentReactionsCountDto:
    comment_id: int
    reactions_count: int


@dataclass
class RepliesCountDto:
    reply_id: int
    replies_count: int
