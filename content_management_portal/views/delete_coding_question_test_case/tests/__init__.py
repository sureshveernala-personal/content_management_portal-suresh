# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_coding_question_test_case"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/{test_case_id}/v1/"

from .test_case_01 import TestCase01DeleteCodingQuestionTestCaseAPITestCase

__all__ = [
    "TestCase01DeleteCodingQuestionTestCaseAPITestCase"
]
