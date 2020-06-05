# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_coding_question_hint"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/hints/v1/"

from .test_case_01 import TestCase01CreateCodingQuestionHintAPITestCase

__all__ = [
    "TestCase01CreateCodingQuestionHintAPITestCase"
]
