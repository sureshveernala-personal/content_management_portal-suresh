import pytest
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionDto, RoughSolutionWithQuestionIdDto, DescriptionDto,\
    QuestionDto, StatementDto, TestCaseWithQuestionIdDto, TestCaseDto,\
    PrefilledCodeWithQuestionIdDto, PrefilledCodeDto, CleanSolutionDto,\
    CleanSolutionWithQuestionIdDto, HintDto, HintWithQuestionIdDto,\
    SolutionApproachDto
from content_management_portal.constants.enums import DescriptionType


@pytest.fixture
def rough_solution_dicts():
    rough_solutions = [
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "rough_solution_id": 1
        },
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "rough_solution_id": 2
        }
    ]
    return rough_solutions


@pytest.fixture
def rough_solution_dtos():
    rough_solution_dtos = [
        RoughSolutionDto(
            language="C", solution_content="string", file_name="string",
            rough_solution_id=1
        ),
        RoughSolutionDto(
            language="C", solution_content="string", file_name="string",
            rough_solution_id=2
        )
    ]
    return rough_solution_dtos


@pytest.fixture
def rough_solution_with_question_id_dicts(rough_solution_dicts):
    rough_solution_with_question_id_dicts = {
        "question_id": 1,
        "rough_solutions": rough_solution_dicts
    }
    return rough_solution_with_question_id_dicts



@pytest.fixture
def rough_solution_with_question_id_dtos(rough_solution_dtos):
    rough_solutions_with_question_id_dtos =[
        RoughSolutionWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            rough_solution_id=1, question_id=1
        ),
        RoughSolutionWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            rough_solution_id=2, question_id=1
        )
    ]
    return rough_solutions_with_question_id_dtos


@pytest.fixture
def description_dict():
    description_dict = {
        "content": "string",
        "content_type": DescriptionType.html.value
    }
    return description_dict

@pytest.fixture
def description_dto():
    description_dto = DescriptionDto(
        content="string",
        content_type=DescriptionType.html.value
    )
    return description_dto

@pytest.fixture
def question_dict(description_dict):
    question_dict = {
        "question_id": 1,
        "short_text": "string",
        "problem_description": description_dict
    }
    return question_dict

@pytest.fixture
def question_dto(description_dto):
    question_dto = QuestionDto(
        short_text="string",
        question_id=1,
        content="string",
        content_type=DescriptionType.html.value
    )
    return question_dto


@pytest.fixture
def statement_dict(description_dict):
    statement_dict = {
        "short_text": "string",
        "problem_description": description_dict
    }
    return statement_dict

@pytest.fixture
def statement_dto(description_dto):
    statement_dto = StatementDto(
        short_text="string",
        content="string",
        content_type=DescriptionType.html.value
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
def test_case_dict():
    test_case_dict = {
        "test_case_number": 1,
        "input": "input",
        "output": "output",
        "score": 0,
        "is_hidden": True,
        "test_case_id": 1
    }
    return test_case_dict


@pytest.fixture
def test_case_with_question_id_dto(test_case_dto):
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
def test_case_with_question_id_dict(test_case_dict):
    test_case_with_question_id_dict = {
        "question_id": 1,
        "test_case": test_case_dict
    }
    return test_case_with_question_id_dict


@pytest.fixture
def prefilled_code_dicts():
    prefilled_codes = [
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "prefilled_code_id": 1
        },
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "prefilled_code_id": 2
        }
    ]
    return prefilled_codes


@pytest.fixture
def prefilled_code_dtos():
    prefilled_code_dtos = [
        PrefilledCodeDto(
            language="C", solution_content="string", file_name="string",
            prefilled_code_id=1
        ),
        PrefilledCodeDto(
            language="C", solution_content="string", file_name="string",
            prefilled_code_id=2
        )
    ]
    return prefilled_code_dtos


@pytest.fixture
def prefilled_code_with_question_id_dicts(prefilled_code_dicts):
    prefilled_code_with_question_id_dicts = {
        "question_id": 1,
        "prefilled_codes": prefilled_code_dicts
    }
    return prefilled_code_with_question_id_dicts



@pytest.fixture
def prefilled_code_with_question_id_dtos(prefilled_code_dtos):
    prefilled_codes_with_question_id_dtos = [
        PrefilledCodeWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            prefilled_code_id=1, question_id=1
        ),
        PrefilledCodeWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            prefilled_code_id=2, question_id=1
        )
    ]
    return prefilled_codes_with_question_id_dtos


@pytest.fixture
def clean_solution_dicts():
    clean_solutions = [
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "clean_solution_id": 1
        },
        {
            "language": "C",
            "solution_content": "string",
            "file_name": "string",
            "clean_solution_id": 2
        }
    ]
    return clean_solutions


@pytest.fixture
def clean_solution_dtos():
    clean_solution_dtos = [
        CleanSolutionDto(
            language="C", solution_content="string", file_name="string",
            clean_solution_id=1
        ),
        CleanSolutionDto(
            language="C", solution_content="string", file_name="string",
            clean_solution_id=2
        )
    ]
    return clean_solution_dtos


@pytest.fixture
def clean_solution_with_question_id_dicts(clean_solution_dicts):
    clean_solution_with_question_id_dicts = {
        "question_id": 1,
        "clean_solutions": clean_solution_dicts
    }
    return clean_solution_with_question_id_dicts



@pytest.fixture
def clean_solution_with_question_id_dtos(clean_solution_dtos):
    clean_solutions_with_question_id_dtos = [
        CleanSolutionWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            clean_solution_id=1, question_id=1
        ),
        CleanSolutionWithQuestionIdDto(
            language="C", solution_content="string", file_name="string",
            clean_solution_id=2, question_id=1
        )
    ]
    return clean_solutions_with_question_id_dtos


@pytest.fixture
def hint_dto(description_dto):
    hint_dto = HintDto(
        hint_id=1,
        title="title",
        hint_number=1,
        content="string",
        content_type=DescriptionType.html.value
    )
    return hint_dto

@pytest.fixture
def hint_dict(description_dict):
    hint_dict = {
        "hint_id": 1,
        "title": "title",
        "hint_number": 1,
        "description": description_dict
    }
    return hint_dict


@pytest.fixture
def hint_with_question_id_dto(hint_dto):
    hint_with_question_id_dto = HintWithQuestionIdDto(
        question_id=1,
        hint_id=1,
        title="title",
        hint_number=1,
        content="string",
        content_type=DescriptionType.html.value
    )
    return hint_with_question_id_dto

@pytest.fixture
def hint_with_question_id_dict(hint_dict):
    hint_with_question_id_dict = {
        "question_id": 1,
        "hint": hint_dict
    }
    return hint_with_question_id_dict


@pytest.fixture
def solution_approach_dict():
    solution_approach_dict = {
        "title": "title",
        "solution_approach_id": 1,
        "description": {
            "content": "content",
            "content_type": DescriptionType.html.value
        },
        "complexity_analysis": {
            "content": "content",
            "content_type": DescriptionType.html.value
        }
    }
    return solution_approach_dict


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
def solution_approach_with_question_id_dict(solution_approach_dict):
    solution_approach_with_question_id_dict = {
        "question_id": 1,
        "solution_approach": solution_approach_dict
    }
    return solution_approach_with_question_id_dict
