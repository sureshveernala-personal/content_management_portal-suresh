from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from content_management_portal.constants.enums import DescriptionType,\
    CodeLanguage
# from content_management_portal.dtos.dtos import DescriptionDto, \
#     RoughSolutionDto, TestCaseDto, PrefilledCodeDto, CleanSolutionDto,\
#     HintDto
    

@dataclass
class DescriptionDto:
    content: str
    content_type: DescriptionType


@dataclass
class SolutionDto:
    language: CodeLanguage
    solution_content: str
    file_name: str


@dataclass
class RoughSolutionDto(SolutionDto):
    rough_solution_id: Optional[int]


@dataclass
class PrefilledCodeDto(SolutionDto):
    prefilled_code_id: Optional[int]


@dataclass
class CleanSolutionDto(SolutionDto):
    clean_solution_id: Optional[int]


@dataclass
class TestCaseDto:
    test_case_id: Optional[int]
    test_case_number: int
    input: str
    output: str
    score: int
    is_hidden: bool


@dataclass
class HintDto:
    hint_id: Optional[int]
    hint_number: int
    title: str
    description: DescriptionDto

@dataclass
class SolutionApproachDto:
    title: str
    solution_approach_id: int
    description_content: str
    description_content_type: str
    complexity_analysis_content: str
    complexity_analysis_content_type: str


####

@dataclass
class StatementDto:
    short_text: str
    problem_description: DescriptionDto


@dataclass
class QuestionDto(StatementDto):
    question_id: int


@dataclass
class RoughSolutionsWithQuestionIdDto:
    question_id: int
    rough_solutions: List[RoughSolutionDto]

@dataclass
class PrefilledCodesWithQuestionIdDto:
    question_id: int
    prefilled_codes: List[PrefilledCodeDto]


@dataclass
class CleanSolutionsWithQuestionIdDto:
    question_id: int
    clean_solutions: List[CleanSolutionDto]


@dataclass
class QuestionStatusDto:
    question_id: int
    statement: str
    rough_solution_status: bool
    test_cases_status: bool
    prefilled_code_status: bool
    solution_approach_status: bool
    clean_solution_status: bool
    hint_status: bool


@dataclass
class QuestionsDto:
    total_questions: int
    offset: int
    limit: int
    questions_list: List[QuestionStatusDto]


@dataclass
class TestCaseWithQuestionIdDto:
    question_id: int
    test_case: TestCaseDto

@dataclass
class HintWithQuestionIdDto:
    question_id: int
    hint: HintDto


@dataclass
class TestCaseIdAndNumberDto:
    test_case_id: int
    test_case_number: int

@dataclass
class TestCasesSwapDetailsDto:
    first_test_case: TestCaseIdAndNumberDto
    second_test_case: TestCaseIdAndNumberDto


@dataclass
class HintIdAndNumberDto:
    hint_id: int
    hint_number: int


@dataclass
class HintsSwapDetailsDto:
    first_hint: HintIdAndNumberDto
    second_hint: HintIdAndNumberDto

