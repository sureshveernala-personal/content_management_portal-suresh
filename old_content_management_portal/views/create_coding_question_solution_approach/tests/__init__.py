# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_coding_question_solution_approach"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/solution_approaches/v1/"

from .test_case_01 import TestCase01CreateCodingQuestionSolutionApproachAPITestCase

__all__ = [
    "TestCase01CreateCodingQuestionSolutionApproachAPITestCase"
]
