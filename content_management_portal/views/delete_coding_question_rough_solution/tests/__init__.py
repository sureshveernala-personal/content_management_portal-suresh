# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_coding_question_rough_solution"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/rough_solutions/{rough_solution_id}/v1/"

from .test_case_01 import TestCase01DeleteCodingQuestionRoughSolutionAPITestCase

__all__ = [
    "TestCase01DeleteCodingQuestionRoughSolutionAPITestCase"
]
