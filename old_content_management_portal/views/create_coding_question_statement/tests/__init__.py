# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_coding_question_statement"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/statement/v1/"

from .test_case_01 import TestCase01CreateCodingQuestionStatementAPITestCase

__all__ = [
    "TestCase01CreateCodingQuestionStatementAPITestCase"
]
