# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_coding_questions"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/v1/"

from .test_case_01 import TestCase01DeleteCodingQuestionsAPITestCase

__all__ = [
    "TestCase01DeleteCodingQuestionsAPITestCase"
]
