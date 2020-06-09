from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from content_management_portal.constants.enums import DescriptionType,\
    CodeLanguage


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
    content: str
    content_type: str

@dataclass
class SolutionApproachDto:
    title: str
    solution_approach_id: int
    description_content: str
    description_content_type: str
    complexity_analysis_content: str
    complexity_analysis_content_type: str


@dataclass
class StatementDto:
    short_text: str
    content: str
    content_type: DescriptionType


@dataclass
class QuestionDto(StatementDto):
    question_id: int


@dataclass
class RoughSolutionWithQuestionIdDto(RoughSolutionDto):
    question_id: int

@dataclass
class PrefilledCodeWithQuestionIdDto(PrefilledCodeDto):
    question_id: int


@dataclass
class CleanSolutionWithQuestionIdDto(CleanSolutionDto):
    question_id: int


@dataclass
class QuestionStatusDto:
    question_id: int
    statement: str
    rough_solution_status: bool
    test_cases_status: bool
    prefilled_code_status: bool
    solution_approach_status: bool
    clean_solution_status: bool


@dataclass
class TestCaseWithQuestionIdDto(TestCaseDto):
    question_id: int

@dataclass
class HintWithQuestionIdDto(HintDto):
    question_id: int


@dataclass
class TestCasesSwapDetailsDto:
    first_test_case_id: int
    first_test_case_number: int
    second_test_case_id: int
    second_test_case_number: int


@dataclass
class HintsSwapDetailsDto:
    first_hint_id: int
    first_hint_number: int
    second_hint_id: int
    second_hint_number: int
