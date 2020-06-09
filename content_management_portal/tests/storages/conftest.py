import pytest
from content_management_portal.models import User, Question, RoughSolution,\
    TestCase, PrefilledCode, CleanSolution, Hint, SolutionApproach
from content_management_portal.constants.enums import \
    DescriptionType, CodeLanguage
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionWithQuestionIdDto, RoughSolutionDto, DescriptionDto,\
    StatementDto, QuestionDto, TestCaseDto, TestCaseWithQuestionIdDto,\
    PrefilledCodeWithQuestionIdDto, PrefilledCodeDto, CleanSolutionDto,\
    CleanSolutionWithQuestionIdDto, HintDto, HintWithQuestionIdDto,\
    TestCasesSwapDetailsDto, HintsSwapDetailsDto, SolutionApproachDto


@pytest.fixture
def user():
    users_list = [
        {
            'username': 'user1',
            "password": "123"
        },
        {
            'username': 'user2',
            "password": "123"
        },
        {
            'username': 'user3',
            "password": "123",
        },
        {
            'username': 'user4',
            "password": "123"
        }
    ]
    user_objs_list = [
        User(
            username=user_dict['username'], password=['password']
        )
        for user_dict in users_list
    ]
    User.objects.bulk_create(user_objs_list)

@pytest.fixture
def user_admin():
    User.objects.create_user(username="user1", password = "123")


@pytest.fixture
def question(user):
    questions_list = [
        {
            "created_by_id": 1,
            "content": "question1",
            "content_type": DescriptionType.text.value,
            "short_text": "short_text1"
        },
        {
            "created_by_id": 1,
            "content": "question2",
            "content_type": DescriptionType.text.value,
            "short_text": "short_text2"
        }
    ]
    question_objs_list = [
        Question(
            created_by_id=question_dict['created_by_id'],
            content=question_dict['content'],
            content_type=question_dict['content_type'],
            short_text=question_dict['short_text']
        )
        for question_dict in questions_list
    ]
    Question.objects.bulk_create(question_objs_list)


@pytest.fixture
def rough_solution(question):
    rough_solution_list = [
        {
            "question_id": 1,
            "language": CodeLanguage.python.value,
            "solution_content": "content",
            "file_name": "file_name"
        }
    ]
    rough_solution_objs_list = [
        RoughSolution(
            question_id=rough_solution_dict['question_id'],
            language=rough_solution_dict['language'],
            solution_content=rough_solution_dict['solution_content'],
            file_name=rough_solution_dict['file_name']
        )
        for rough_solution_dict in rough_solution_list
    ]
    RoughSolution.objects.bulk_create(rough_solution_objs_list)


@pytest.fixture
def prefilled_code(question):
    prefilled_code_list = [
        {
            "question_id": 1,
            "language": CodeLanguage.python.value,
            "solution_content": "content",
            "file_name": "file_name"
        }
    ]
    prefilled_code_objs_list = [
        PrefilledCode(
            question_id=prefilled_code_dict['question_id'],
            language=prefilled_code_dict['language'],
            solution_content=prefilled_code_dict['solution_content'],
            file_name=prefilled_code_dict['file_name']
        )
        for prefilled_code_dict in prefilled_code_list
    ]
    PrefilledCode.objects.bulk_create(prefilled_code_objs_list)


@pytest.fixture
def clean_solution(question):
    clean_solution_list = [
        {
            "question_id": 1,
            "language": CodeLanguage.python.value,
            "solution_content": "content",
            "file_name": "file_name"
        }
    ]
    clean_solution_objs_list = [
        CleanSolution(
            question_id=clean_solution_dict['question_id'],
            language=clean_solution_dict['language'],
            solution_content=clean_solution_dict['solution_content'],
            file_name=clean_solution_dict['file_name']
        )
        for clean_solution_dict in clean_solution_list
    ]
    CleanSolution.objects.bulk_create(clean_solution_objs_list)


@pytest.fixture
def test_case(question):
    test_cases_list = [
        {
            "question_id": 1,
            "test_case_number": 1,
            "input": "input",
            "output": "output",
            "score": 0,
            "is_hidden": True
        },
        {
            "question_id": 1,
            "test_case_number": 2,
            "input": "input",
            "output": "output",
            "score": 0,
            "is_hidden": True
        },
        {
            "question_id": 1,
            "test_case_number": 3,
            "input": "input",
            "output": "output",
            "score": 0,
            "is_hidden": True
        }
    ]
    test_case_objs_list = [
        TestCase(
            question_id=test_cases_dict['question_id'],
            test_case_number=test_cases_dict['test_case_number'],
            input=test_cases_dict['input'],
            output=test_cases_dict['output'],
            score=test_cases_dict['score'],
            is_hidden=test_cases_dict['question_id']
        )
        for test_cases_dict in test_cases_list
    ]
    TestCase.objects.bulk_create(test_case_objs_list)


@pytest.fixture
def hint(question):
    hints_list = [
        {
            "question_id": 1,
            "hint_number": 1,
            "content": "content",
            "content_type": DescriptionType.html.value,
            "title": "title"
        },
        {
            "question_id": 1,
            "hint_number": 2,
            "content": "content",
            "content_type": DescriptionType.html.value,
            "title": "title"
        },
        {
            "question_id": 1,
            "hint_number": 3,
            "content": "content",
            "content_type": DescriptionType.html.value,
            "title": "title"
        },
    ]
    hint_objs_list = [
        Hint(
            question_id=hint_dict['question_id'],
            hint_number=hint_dict['hint_number'],
            content=hint_dict['content'],
            content_type=hint_dict['content_type'],
            title=hint_dict['title']
        )
        for hint_dict in hints_list
    ]
    Hint.objects.bulk_create(hint_objs_list)


@pytest.fixture
def solution_approach(question):
    solution_approach_list = [
        {
            "question_id": 1,
            "title": "title",
            "description_content": "content",
            "description_content_type": DescriptionType.html.value,
            "complexity_analysis_content": "content",
            "complexity_analysis_content_type": DescriptionType.html.value
        }
    ]
    solution_approach_objs_list = [
        SolutionApproach(
            question_id=solution_approach['question_id'],
            title=solution_approach['title'],
            description_content=solution_approach['description_content'],
            description_content_type=solution_approach[
                'description_content_type'
            ],
            complexity_analysis_content=solution_approach[
                'complexity_analysis_content'
            ],
            complexity_analysis_content_type=solution_approach[
                'complexity_analysis_content_type'
            ]
        )
        for solution_approach in solution_approach_list
    ]
    SolutionApproach.objects.bulk_create(solution_approach_objs_list)


@pytest.fixture
def rough_solutions_with_question_id_dtos(rough_solution_dtos):
    rough_solution_with_question_id_dtos = [
        RoughSolutionWithQuestionIdDto(
            language=CodeLanguage.python.value,
            solution_content="content",
            file_name="file_name",
            rough_solution_id=1,
            question_id=1
        )
    ]
    return rough_solution_with_question_id_dtos

@pytest.fixture
def rough_solution_dtos():
    rough_solution_dtos = [
        RoughSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            rough_solution_id=1
        ),
        RoughSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            rough_solution_id=None
        )
    ]
    return rough_solution_dtos


@pytest.fixture
def updated_rough_solution_dtos():
    rough_solution_dtos = [
        RoughSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="New_content", file_name="New_file_name",
            rough_solution_id=1
        ),
    ]
    return rough_solution_dtos



@pytest.fixture
def description_dict():
    description_dict = {
        "content": "question1",
        "content_type": DescriptionType.text.value
    }
    return description_dict

@pytest.fixture
def description_dto():
    description_dto =  DescriptionDto(
        content="question1",
        content_type=DescriptionType.text.value
    )
    return description_dto

@pytest.fixture
def updated_description_dto():
    description_dto =  DescriptionDto(
        content="new_question1",
        content_type=DescriptionType.html.value
    )
    return description_dto

@pytest.fixture
def question_dict(description_dict):
    question_dict = {
        "question_id": 1,
        "short_text": "short_text1",
        "problem_description": description_dict
    }
    return question_dict

@pytest.fixture
def question_dto(description_dto):
    question_dto = QuestionDto(
        short_text="short_text1",
        question_id=1,
        content="question1",
        content_type=DescriptionType.text.value
    )
    return question_dto


@pytest.fixture
def updated_question_dto(updated_description_dto):
    question_dto = QuestionDto(
        short_text="new_short_text1",
        question_id=1,
        content="new_question1",
        content_type=DescriptionType.html.value
    )
    return question_dto

@pytest.fixture
def statement_dict(description_dict):
    statement_dict = {
        "short_text": "short_text1",
        "problem_description": description_dict
    }
    return statement_dict

@pytest.fixture
def statement_dto(description_dto):
    statement_dto = StatementDto(
        short_text="short_text1",
        problem_description=description_dto
    )
    return statement_dto

@pytest.fixture
def test_case_dto():
    test_case_dto = TestCaseDto(
        test_case_id=1,
        input="input",
        output="output",
        score=0,
        is_hidden=True,
        test_case_number=1
    )
    return test_case_dto

@pytest.fixture
def test_case_dtos():
    test_case_dto = [
        TestCaseDto(
            test_case_id=1,
            input="input",
            output="output",
            score=0,
            is_hidden=True,
            test_case_number=1
        ),
        TestCaseDto(
            test_case_id=2,
            input="input",
            output="output",
            score=0,
            is_hidden=True,
            test_case_number=2
        ),
        TestCaseDto(
            test_case_id=3,
            input="input",
            output="output",
            score=0,
            is_hidden=True,
            test_case_number=3
        )
    ]
    return test_case_dto


@pytest.fixture
def updated_test_case_dto():
    test_case_dto = TestCaseDto(
        test_case_id=1,
        input="new_input",
        output="new_output",
        score=10,
        is_hidden=False,
        test_case_number=2
    )
    return test_case_dto


@pytest.fixture
def test_case_dto_without_test_case_id():
    test_case_dto = TestCaseDto(
        test_case_id=None,
        input="input",
        output="output",
        score=0,
        is_hidden=True,
        test_case_number=1
    )
    return test_case_dto


@pytest.fixture
def test_case_with_question_id_dto():
    test_case_with_question_id_dto = TestCaseWithQuestionIdDto(
        question_id=1,
        test_case_id=1,
        input="input",
        output="output",
        score=0,
        is_hidden=True,
        test_case_number=1
    )
    return test_case_with_question_id_dto

@pytest.fixture
def updted_test_case_with_question_id_dto(updated_test_case_dto):
    test_case_with_question_id_dto = TestCaseWithQuestionIdDto(
        question_id=1,
        test_case_id=1,
        input="new_input",
        output="new_output",
        score=10,
        is_hidden=False,
        test_case_number=2
    )
    return test_case_with_question_id_dto


@pytest.fixture
def prefilled_codes(prefilled_code_dtos):
    prefilled_code_with_question_id_dtos = [
        PrefilledCodeWithQuestionIdDto(
            question_id=1,
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            prefilled_code_id=1
        )
    ]
    return prefilled_code_with_question_id_dtos


@pytest.fixture
def prefilled_code_dtos():
    prefilled_code_dtos = [
        PrefilledCodeDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            prefilled_code_id=1
        ),
        PrefilledCodeDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            prefilled_code_id=None
        )
    ]
    return prefilled_code_dtos


@pytest.fixture
def updated_prefilled_code_dtos():
    prefilled_code_dtos = [
        PrefilledCodeDto(
            language=CodeLanguage.python.value,
            solution_content="New_content", file_name="New_file_name",
            prefilled_code_id=1
        ),
    ]
    return prefilled_code_dtos

@pytest.fixture
def prefilled_codes_with_question_id_dtos(prefilled_code_dtos):
    prefilled_codes_with_question_id_dtos = [
        PrefilledCodeWithQuestionIdDto(
            question_id=1,
            language=CodeLanguage.python.value,
            solution_content="content",
            file_name="file_name",
            prefilled_code_id=1
        )
    ]
    return prefilled_codes_with_question_id_dtos

@pytest.fixture
def clean_solutions(clean_solution_dtos):
    clean_solution_with_question_id_dtos = [
        CleanSolutionWithQuestionIdDto(
            question_id=1,
            language=CodeLanguage.python.value,
            solution_content="content",
            file_name="file_name",
            clean_solution_id=1
        )
    ]
    return clean_solution_with_question_id_dtos


@pytest.fixture
def clean_solution_dtos():
    clean_solution_dtos = [
        CleanSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            clean_solution_id=1
        ),
        CleanSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="content", file_name="file_name",
            clean_solution_id=None
        )
    ]
    return clean_solution_dtos


@pytest.fixture
def updated_clean_solution_dtos():
    clean_solution_dtos = [
        CleanSolutionDto(
            language=CodeLanguage.python.value,
            solution_content="New_content", file_name="New_file_name",
            clean_solution_id=1
        ),
    ]
    return clean_solution_dtos


@pytest.fixture
def clean_solutions_with_question_id_dtos(clean_solution_dtos):
    clean_solutions_with_question_id_dtos = [
        CleanSolutionWithQuestionIdDto(
            question_id=1,
            language=CodeLanguage.python.value,
            solution_content="content",
            file_name="file_name",
            clean_solution_id=1
        )
    ]
    return clean_solutions_with_question_id_dtos

@pytest.fixture
def hint_description_dict():
    description_dict = {
        "content": "content",
        "content_type": DescriptionType.html.value
    }
    return description_dict


@pytest.fixture
def hint_description_dto():
    description_dto = DescriptionDto(
        content="content",
        content_type=DescriptionType.html.value
    )
    return description_dto



@pytest.fixture
def hint_dto(hint_description_dto):
    hint_dto = HintDto(
        hint_id=1,
        title="title",
        content="content",
        content_type=DescriptionType.html.value,
        hint_number=1
    )
    return hint_dto

@pytest.fixture
def hint_dtos(hint_description_dto):
    hint_dto = [
        HintDto(
            hint_id=1,
            title="title",
            content="content",
            content_type=DescriptionType.html.value,
            hint_number=1
        ),
        HintDto(
            hint_id=2,
            title="title",
            content="content",
            content_type=DescriptionType.html.value,
            hint_number=2
        ),
        HintDto(
            hint_id=3,
            title="title",
            content="content",
            content_type=DescriptionType.html.value,
            hint_number=3
        )
    ]
    return hint_dto


@pytest.fixture
def updated_hint_dto():
    hint_dto = HintDto(
        hint_id=1,
        title="title",
        content="new_content",
        content_type=DescriptionType.html.value,
        hint_number=2
    )
    return hint_dto


@pytest.fixture
def hint_dto_without_hint_id(hint_description_dto):
    hint_dto = HintDto(
        hint_id=None,
        title="title",
        content="content",
        content_type=DescriptionType.html.value,
        hint_number=1
    )
    return hint_dto


@pytest.fixture
def hint_with_question_id_dto(hint_dto):
    hint_with_question_id_dto = HintWithQuestionIdDto(
        question_id=1,
        hint_id=1,
        title="title",
        content="content",
        content_type=DescriptionType.html.value,
        hint_number=1
    )
    return hint_with_question_id_dto

@pytest.fixture
def updted_hint_with_question_id_dto(updated_hint_dto):
    hint_with_question_id_dto = HintWithQuestionIdDto(
        question_id=1,
        hint_id=1,
        title="title",
        content="new_content",
        content_type=DescriptionType.html.value,
        hint_number=2
    )
    return hint_with_question_id_dto


@pytest.fixture
def test_cases_swap_details_dto():
    test_cases_swap_details_dto = TestCasesSwapDetailsDto(
        first_test_case_id=1,
        first_test_case_number=2,
        second_test_case_id=2,
        second_test_case_number=1
    )
    return test_cases_swap_details_dto


@pytest.fixture
def hints_swap_details_dto():
    hints_swap_details_dto = HintsSwapDetailsDto(
        first_hint_id=1,
        first_hint_number=2,
        second_hint_id=2,
        second_hint_number=1
    )
    return hints_swap_details_dto

@pytest.fixture
def solution_approach_dto():
    solution_approach_dto = SolutionApproachDto(
        solution_approach_id=1,
        title="title",
        description_content="content",
        description_content_type=DescriptionType.html.value,
        complexity_analysis_content="content",
        complexity_analysis_content_type=DescriptionType.html.value
    )
    return solution_approach_dto


@pytest.fixture
def updated_solution_approach_dto():
    solution_approach_dto = SolutionApproachDto(
        solution_approach_id=1,
        title="new_title",
        description_content="new_content",
        description_content_type=DescriptionType.html.value,
        complexity_analysis_content="new_content",
        complexity_analysis_content_type=DescriptionType.html.value
    )
    return solution_approach_dto