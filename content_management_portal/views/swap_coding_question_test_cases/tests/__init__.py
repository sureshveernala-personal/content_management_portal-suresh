# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "swap_coding_question_test_cases"
REQUEST_METHOD = "put"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/swap/v1/"

from .test_case_01 import TestCase01SwapCodingQuestionTestCasesAPITestCase

__all__ = [
    "TestCase01SwapCodingQuestionTestCasesAPITestCase"
]
