# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "get_coding_questions"
REQUEST_METHOD = "get"
URL_SUFFIX = "coding_questions/v1/"

from .test_case_01 import TestCase01GetCodingQuestionsAPITestCase

__all__ = [
    "TestCase01GetCodingQuestionsAPITestCase"
]
