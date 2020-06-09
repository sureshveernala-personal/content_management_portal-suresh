# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_coding_question_prefilled_code"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/{prefilled_code_id}/v1/"

from .test_case_01 import TestCase01DeleteCodingQuestionPrefilledCodeAPITestCase

__all__ = [
    "TestCase01DeleteCodingQuestionPrefilledCodeAPITestCase"
]
