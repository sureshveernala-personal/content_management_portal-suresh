from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
import pytest
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.get_posts_interactor import GetPostsInteractor


def test_get_posts_interactor_with_invalid_post_ids():
    # Arrange
    post_ids = [1, 2]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostsInteractor(storage=storage)
    storage.get_total_post_ids.return_value = [3, 4]
    presenter.raise_invalid_post_ids_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

    #Assert
    kwargs = presenter.raise_invalid_post_ids_exception.call_args.kwargs
    error = kwargs['error']
    actual_post_ids = error.post_ids
    assert post_ids == actual_post_ids


def test_get_posts_interactor_with_valid_details(
        post_dtos, post_tag_dtos, post_reactions_count_dtos,
        comments_count_dtos, comment_dtos, comment_reactions_count_dtos,
        replies_count_dtos, user_dtos, post_details_dto
    ):
    # Arrange
    post_ids = [1, 2]
    comment_ids= [1, 2]
    user_ids= [1, 2]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostsInteractor(storage=storage)
    storage.get_total_post_ids.return_value = [1, 2]
    storage.get_posts.return_value = post_dtos
    storage.get_post_tags.return_value = post_tag_dtos
    storage.get_post_reactions_count.return_value = post_reactions_count_dtos
    storage.get_comments_count.return_value = comments_count_dtos
    storage.get_latest_comments.side_effect = \
        [comment_dtos[:1], comment_dtos[1:]]
    storage.get_comment_reactions_count.return_value = \
        comment_reactions_count_dtos
    storage.get_replies_count.return_value = replies_count_dtos
    storage.get_users_details.return_value = user_dtos
    presenter.get_posts_response.return_value = "get_posts"

    # Act
    response = interactor.get_posts_wrapper(
        post_ids=post_ids, presenter=presenter
    )

    #Assert
    storage.get_total_post_ids.assert_called_once()
    storage.get_posts.assert_called_once_with(post_ids=post_ids)
    storage.get_post_tags.assert_called_once_with(post_ids=post_ids)
    storage.get_post_reactions_count.assert_called_once_with(post_ids=post_ids)
    storage.get_comments_count.assert_called_once_with(post_ids=post_ids)
    first_time_argument = storage.get_latest_comments.call_args_list[0].kwargs
    second_time_argument = storage.get_latest_comments.call_args_list[1].kwargs
    assert first_time_argument['post_id'] == 1
    assert first_time_argument['limit'] == 2
    assert second_time_argument['post_id'] == 2
    assert second_time_argument['limit'] == 2
    storage.get_comment_reactions_count.\
        assert_called_once_with(comment_ids=comment_ids)
    storage.get_replies_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_users_details.assert_called_once_with(user_ids=user_ids)
    presenter.get_posts_response.assert_called_once_with(
        post_details_dto=post_details_dto
    )
    assert response == "get_posts"
