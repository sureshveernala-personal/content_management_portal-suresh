"""
Delete CleanSolution with invalid Question Id
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal.utils.custom_test_utils import CustomTestUtils


REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"clean_solution_id": "1234", "question_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01DeleteCodingQuestionCleanSolutionAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username: str, password: str):
        super(TestCase01DeleteCodingQuestionCleanSolutionAPITestCase, self)\
            .setupUser(username=username, password=password)

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.