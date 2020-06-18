import pytest
from datetime import datetime
from gyaan.interactors.storages.dtos import DomainDto, DomainStatsDto,\
    UserDto, JoiningRequestDto, PostDto, PostTagDto, PostReactionsCountDto,\
    CommentsCountDto, CommentDto, CommentReactionsCountDto, RepliesCountDto
from gyaan.interactors.presenters.dtos import DomainDetailsDTO,\
    PostDetailsDto, DomainDetailsWithPostsDto


@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDto(
            user_id=1, user_name="suresh", profile_pic="www.sures_pic.com"
        ),
        UserDto(
            user_id=2, user_name="suresh", profile_pic="www.sures_pic.com"
        )
    ]
    return user_dtos


@pytest.fixture
def joining_requested_users():
    user_dtos = [
        UserDto(
            user_id=3, user_name="suresh", profile_pic="www.sures_pic.com"
        ),
        UserDto(
            user_id=4, user_name="suresh", profile_pic="www.sures_pic.com"
        )
    ]
    return user_dtos


@pytest.fixture
def domain_dto():
    domain_dto = DomainDto(
        domain_id=1, title="title", description="description"
    )
    return domain_dto


@pytest.fixture
def domain_stats_dtos():
    domain_stats_dtos = [
        DomainStatsDto(
            domain_id=1, posts_count=2, members_count=2, bookmark_count=2
        ),
        DomainStatsDto(
            domain_id=2, posts_count=2, members_count=2, bookmark_count=2
        )
    ]
    return domain_stats_dtos


@pytest.fixture
def joining_request_dtos():
    joining_request_dtos = [
        JoiningRequestDto(joining_request_id=1, user_id=3),
        JoiningRequestDto(joining_request_id=2, user_id=4)
    ]
    return joining_request_dtos


@pytest.fixture
def domain_details_dto(
        domain_dto, domain_stats_dtos, user_dtos, joining_request_dtos,
        joining_requested_users
    ):
    domain_details_dto = DomainDetailsDTO(
        domain_id=1,
        domain_dto=domain_dto,
        user_id=1,
        domain_stats=domain_stats_dtos,
        expert_users=user_dtos,
        is_user_domain_expert=True,
        domain_join_requests=joining_request_dtos,
        joining_requested_users=joining_requested_users
    )
    return domain_details_dto


@pytest.fixture
def domain_details_dto_when_user_not_expert(
        domain_dto, domain_stats_dtos, user_dtos, joining_request_dtos,
        joining_requested_users
    ):
    domain_details_dto = DomainDetailsDTO(
        domain_id=1,
        domain_dto=domain_dto,
        user_id=2,
        domain_stats=domain_stats_dtos,
        expert_users=user_dtos[:1],
        is_user_domain_expert=False,
        domain_join_requests=[],
        joining_requested_users=[]
    )
    return domain_details_dto


@pytest.fixture
def post_dtos():
    post_dtos = [
            PostDto(
            post_id=1,
            title="title",
            content="content",
            posted_at=datetime.now(),
            posted_by_id=1
        ),
        PostDto(
            post_id=2,
            title="title_2",
            content="content_2",
            posted_at=datetime.now(),
            posted_by_id=1
        )
    ]
    return post_dtos


@pytest.fixture
def post_tag_dtos():
    post_tag_dtos = [
        PostTagDto(post_id=1, tag_id=1, name="tag1"),
        PostTagDto(post_id=2, tag_id=2, name="tag2")
    ]
    return post_tag_dtos



@pytest.fixture
def post_reactions_count_dtos():
    post_reactions_count_dtos = [
        PostReactionsCountDto(post_id=1, reactions_count=2),
        PostReactionsCountDto(post_id=2, reactions_count=2)
    ]
    return post_reactions_count_dtos



@pytest.fixture
def comments_count_dtos():
    comments_count_dtos = [
        CommentsCountDto(comment_id=1, comments_count=2),
        CommentsCountDto(comment_id=2, comments_count=2)
    ]
    return comments_count_dtos


@pytest.fixture
def comment_dtos():
    comment_dtos = [
        CommentDto(
            comment_id=1,
            content="content",
            commented_at=datetime.now,
            commented_by_id=1,
            post_id=1
        ),
        CommentDto(
            comment_id=2,
            content="content",
            commented_at=datetime.now,
            commented_by_id=2,
            post_id=2
        )
    ]
    return comment_dtos


@pytest.fixture
def comment_reactions_count_dtos():
    comment_reactions_count_dtos = [
        CommentReactionsCountDto(comment_id=1, reactions_count=2),
        CommentReactionsCountDto(comment_id=2, reactions_count=2)
    ]
    return comment_reactions_count_dtos


@pytest.fixture
def replies_count_dtos():
    replies_count_dtos = [
        RepliesCountDto(reply_id=1, replies_count=2),
        RepliesCountDto(reply_id=2, replies_count=2)
    ]
    return replies_count_dtos


@pytest.fixture
def post_details_dto(
        post_dtos, post_tag_dtos, post_reactions_count_dtos,
        comments_count_dtos, comment_dtos, comment_reactions_count_dtos,
        replies_count_dtos, user_dtos
    ):
    post_details_dto = PostDetailsDto(
        post_dtos=post_dtos,
        post_tags=post_tag_dtos,
        post_reaction_counts=post_reactions_count_dtos,
        comments_counts=comments_count_dtos,
        comment_dtos=comment_dtos,
        comment_reactions_counts=comment_reactions_count_dtos,
        replies_counts=replies_count_dtos,
        user_dtos=user_dtos
    )
    return post_details_dto


@pytest.fixture
def domain_details_with_posts_dto(post_details_dto, domain_details_dto):
    domain_details_with_posts_dto = DomainDetailsWithPostsDto(
        post_details_dto=post_details_dto,
        domain_details_dto=domain_details_dto
    )
    return domain_details_with_posts_dto
