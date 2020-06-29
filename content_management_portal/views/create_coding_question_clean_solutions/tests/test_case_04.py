"""
Test Create CleanSolution with valid details
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal.utils.custom_test_utils import CustomTestUtils
from content_management_portal.models import CleanSolution
from freezegun import freeze_time


REQUEST_BODY = """
[
    {
        "language": "PYTHON",
        "solution_content": "string",
        "file_name": "string",
        "clean_solution_id": 1
    },
    {
        "language": "PYTHON",
        "solution_content": "string",
        "file_name": "string",
        "clean_solution_id": null
    }
]
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


class TestCase04CreateCodingQuestionCleanSolutionsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username: str, password: str):
        super(TestCase04CreateCodingQuestionCleanSolutionsAPITestCase, self)\
        .setupUser(username=username, password=password)

        self.create_clean_solutions()


    @freeze_time('2020-1-1')
    def test_case(self):
        self.default_test_case()
        clean_solution_1 = CleanSolution.objects.get(id=1)
        clean_solution_2 = CleanSolution.objects.get(id=4)
        self.assert_match_snapshot(clean_solution_1.language)
        self.assert_match_snapshot(clean_solution_1.file_name)
        self.assert_match_snapshot(clean_solution_1.solution_content)
        self.assert_match_snapshot(clean_solution_1.created_at)
        self.assert_match_snapshot(clean_solution_1.question)
        self.assert_match_snapshot(clean_solution_2.language)
        self.assert_match_snapshot(clean_solution_2.file_name)
        self.assert_match_snapshot(clean_solution_2.solution_content)
        self.assert_match_snapshot(clean_solution_2.created_at)
        self.assert_match_snapshot(clean_solution_2.question)
