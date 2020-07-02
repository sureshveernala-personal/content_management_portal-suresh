from datetime import datetime
import factory
from content_management_portal.models import Question, CleanSolution,\
    Hint, PrefilledCode, RoughSolution, SolutionApproach, TestCase
from content_management_portal.constants.enums import DescriptionType,\
    CodeLanguage, DescriptionTypeList, CodeLanguageList


class QuestionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Question

    created_by_id = factory.Sequence(lambda number: number+1)
    short_text = factory.Sequence(lambda number: f"short_text_{number+1}")
    content = factory.Sequence(lambda number: f"content_{number+1}")
    content_type = factory.Iterator(DescriptionTypeList)
    created_at = factory.LazyFunction(datetime.now)


class SolutionFactory(factory.django.DjangoModelFactory):

    language = factory.Iterator(CodeLanguageList)
    solution_content = factory.Sequence(
        lambda number: f"solution_content{number+1}"
    )
    file_name = factory.Sequence(lambda number: f"file_name_{number+1}")
    created_at = factory.LazyFunction(datetime.now)
    question = factory.SubFactory(QuestionFactory)


class CleanSolutionFactory(SolutionFactory):

    class Meta:
        model = CleanSolution


class RoughSolutionFactory(SolutionFactory):

    class Meta:
        model = RoughSolution


class PrefilledCodeFactory(SolutionFactory):

    class Meta:
        model = PrefilledCode


class TestCaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TestCase


    test_case_number = factory.Sequence(lambda number: number+1)
    input = factory.Sequence(lambda number: f"input_{number+1}")
    output = factory.Sequence(lambda number: f"output_{number+1}")
    score = factory.Iterator([100, 95, 90, 75])
    is_hidden = factory.Iterator([True, False])
    created_at = factory.LazyFunction(datetime.now)
    question = factory.SubFactory(QuestionFactory)


class HintFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Hint

    hint_number = factory.Sequence(lambda number: number+1)
    title = factory.Sequence(lambda number: f"title{number+1}")
    content = factory.Sequence(lambda number: f"content_{number+1}")
    content_type = factory.Iterator(DescriptionTypeList)
    created_at = factory.LazyFunction(datetime.now)
    question = factory.SubFactory(QuestionFactory)


class SolutionApproachFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SolutionApproach

    title = factory.Sequence(lambda number: f"title{number+1}")
    description_content =  factory.Sequence(
        lambda number: f"description_content_{number+1}"
    )
    description_content_type = factory.Iterator(DescriptionTypeList)
    complexity_analysis_content =  factory.Sequence(
        lambda number: f"complexity_analysis_content_{number+1}"
    )
    complexity_analysis_content_type = factory.Iterator(DescriptionTypeList)
    created_at = factory.LazyFunction(datetime.now)
    question = factory.SubFactory(QuestionFactory)
