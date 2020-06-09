# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_coding_question_test_case"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/v1/"

from .test_case_01 import TestCase01CreateCodingQuestionTestCaseAPITestCase

__all__ = [
    "TestCase01CreateCodingQuestionTestCaseAPITestCase"
]
