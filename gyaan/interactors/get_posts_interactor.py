from typing import List
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.presenters.dtos import PostDetailsDto,PostDto
from gyaan.interactors.storages.dtos import PostDto


class GetPostsInteractor():
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(
            self, post_ids: List[int],presenter: PresenterInterface,
        ):
        try:
            response = self._prepare_posts_response(
                post_ids=post_ids, presenter=presenter
            )
            return response
        except InvalidPostIds as error:
            presenter.raise_invalid_post_ids_exception(error=error)

    def _prepare_posts_response(
            self, post_ids: List[int], presenter: PresenterInterface,
        ):
        post_details_dto = self.get_posts(post_ids=post_ids)
        response = presenter.get_posts_response(
            post_details_dto=post_details_dto
        )
        return response

    def get_posts(self, post_ids: List[int]):
        self._validate_post_ids(post_ids=post_ids)
        unique_post_ids = list(set(post_ids))
        post_ids = unique_post_ids
        post_dtos = self.storage.get_posts(post_ids=post_ids)
        post_tags = self.storage.get_post_tags(post_ids=post_ids)
        post_reaction_count = \
            self.storage.get_post_reactions_count(post_ids=post_ids)

        comments_count, comment_dtos, comment_reactions_count,\
        replies_count, commented_user_ids = \
            self._get_comments_details(post_ids=post_ids)

        posted_user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids = sorted(list(set(posted_user_ids + commented_user_ids)))
        user_dtos = self.storage.get_users_details(user_ids=user_ids)

        post_details_dto = PostDetailsDto(
            post_dtos=post_dtos,
            post_tags=post_tags,
            post_reaction_counts=post_reaction_count,
            comments_counts=comments_count,
            comment_dtos=comment_dtos,
            comment_reactions_counts=comment_reactions_count,
            replies_counts=replies_count,
            user_dtos=user_dtos
        )
        return post_details_dto

    def _validate_post_ids(self, post_ids: List[int]):
        total_post_ids = self.storage.get_total_post_ids()
        invalid_post_ids = [
            post_id
            for post_id in post_ids
            if post_id not in total_post_ids
        ]
        if invalid_post_ids:
            raise InvalidPostIds(post_ids=post_ids)


    def _get_comments_details(self, post_ids: List[int]):
        comments_count = self.storage.get_comments_count(post_ids=post_ids)
        comment_dtos = []
        for post_id in post_ids:
            comment_dtos += \
                self.storage.get_latest_comments(post_id=post_id, limit=2)

        comment_ids = [comment_dto.comment_id for comment_dto in comment_dtos]

        comment_reactions_count = \
            self.storage.get_comment_reactions_count(comment_ids=comment_ids)

        replies_count = self.storage.get_replies_count(comment_ids=comment_ids)

        commented_user_ids = \
            [comment_dto.commented_by_id for comment_dto in comment_dtos]

        return (
            comments_count, comment_dtos, comment_reactions_count,
            replies_count, commented_user_ids
        )
