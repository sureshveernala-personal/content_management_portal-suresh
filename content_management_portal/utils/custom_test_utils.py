from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from content_management_portal.models import Question, CleanSolution,\
    Hint, PrefilledCode, RoughSolution, SolutionApproach, TestCase
from content_management_portal.factories.factories import QuestionFactory,\
    CleanSolutionFactory, HintFactory, PrefilledCodeFactory,\
    RoughSolutionFactory, SolutionApproachFactory, TestCaseFactory


class CustomTestUtils(CustomAPITestCase):

    @freeze_time('2020-1-1')
    def create_questions(self):
        QuestionFactory.reset_sequence(0)
        QuestionFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_clean_solutions(self):
        CleanSolutionFactory.reset_sequence(0)
        CleanSolutionFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_rough_solutions(self):
        RoughSolutionFactory.reset_sequence(0)
        RoughSolutionFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_prefilled_codes(self):
        PrefilledCodeFactory.reset_sequence(0)
        PrefilledCodeFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_hints(self):
        HintFactory.reset_sequence(0)
        HintFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_test_cases(self):
        TestCaseFactory.reset_sequence(0)
        TestCaseFactory.create_batch(size=3)


    @freeze_time('2020-1-1')
    def create_solution_approaches(self):
        SolutionApproachFactory.reset_sequence(0)
        SolutionApproachFactory.create_batch(size=3)
