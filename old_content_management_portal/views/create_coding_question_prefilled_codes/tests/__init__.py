# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_coding_question_prefilled_codes"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/v1/"

from .test_case_01 import TestCase01CreateCodingQuestionPrefilledCodesAPITestCase

__all__ = [
    "TestCase01CreateCodingQuestionPrefilledCodesAPITestCase"
]
