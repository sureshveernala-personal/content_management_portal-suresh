import pytest
from content_management_portal_auth.models import User
from content_management_portal_auth.interactors.storages.dtos import\
    UserDto


@pytest.fixture
def create_users():
    users_list = [
        {
            'username': 'user1',
            "password": "123"
        },
        {
            'username': 'user2',
            "password": "123"
        },
        {
            'username': 'user3',
            "password": "123",
        },
        {
            'username': 'user4',
            "password": "123"
        }
    ]
    user_objs_list = [
        User(
            username=user_dict['username'], password=['password']
        )
        for user_dict in users_list
    ]
    User.objects.bulk_create(user_objs_list)

@pytest.fixture
def create_user_admin():
    User.objects.create_user(username="user1", password = "123")


@pytest.fixture
def create_user_dtos():
    user_dtos = [
        UserDto(username="user1", user_id=1),
        UserDto(username="user2", user_id=2),
        UserDto(username="user3", user_id=3)
    ]
    return user_dtos
