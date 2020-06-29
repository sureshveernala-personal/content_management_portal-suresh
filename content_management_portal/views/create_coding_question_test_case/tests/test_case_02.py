"""
Create TestCase with Invalid TestCase Id return NotFound
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal.utils.custom_test_utils import CustomTestUtils


REQUEST_BODY = """
{
    "test_case_number": 1,
    "input": "string",
    "output": "string",
    "score": 1,
    "is_hidden": true,
    "test_case_id": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"question_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02CreateCodingQuestionTestCaseAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    def setupUser(self, username: str, password: str):
        super(TestCase02CreateCodingQuestionTestCaseAPITestCase, self)\
            .setupUser(username=username, password=password)

        self.create_questions()

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.