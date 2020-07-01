"""
Test Login with invalid password
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal_auth.models import User
import json
from freezegun import freeze_time
from unittest.mock import patch
from common.dtos import UserAuthTokensDTO
from datetime import datetime


REQUEST_BODY = """
{
    "username": "suresh",
    "password": "12345"
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


class TestCase03LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self):
        username="suresh"
        password = "1234"
        User.objects.create_superuser(
            username=username,
            password=password,
            email=""
        )


    def test_case(self):
        self.setupUser()
        self.default_test_case()
