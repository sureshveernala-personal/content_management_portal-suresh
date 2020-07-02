"""
Test Login with valid details
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal_auth.models import User
from freezegun import freeze_time
from unittest.mock import patch
from common.dtos import UserAuthTokensDTO
from datetime import datetime


REQUEST_BODY = """
{
    "username": "suresh",
    "password": "123456"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self):
        username="suresh"
        password = "123456"
        User.objects.create_superuser(
            username=username,
            password=password,
            email=""
        )


    @patch("common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens")
    def test_case(self, create_user_auth_tokens):
        access_token_dto = UserAuthTokensDTO(
            user_id=1,
            access_token='PbWOleEjL99tOoUPfPY3NR2rA9mphk',
            refresh_token='sFajX39Y1Ye9AjKUd2zKn3Yf4syryD',
            expires_in=datetime(2337, 4, 20, 2, 14, 3, 493790)
        )
        create_user_auth_tokens.return_value = access_token_dto
        self.setupUser()
