import pytest
from content_management_portal_auth.models import User


@pytest.fixture
def user():
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
def user_admin():
    User.objects.create_user(username="user1", password = "123")
