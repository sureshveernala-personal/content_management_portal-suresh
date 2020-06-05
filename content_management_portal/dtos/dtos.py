from content_management_portal.interactors.storages.dtos import *

# from datetime import datetime
# from dataclasses import dataclass
# from typing import List, Optional
# from content_management_portal.constants.enums import DescriptionType,\
#     CodeLanguage


# @dataclass
# class DescriptionDto:
#     content: str
#     content_type: DescriptionType


# @dataclass
# class SolutionDto:
#     language: CodeLanguage
#     solution_content: str
#     file_name: str


# @dataclass
# class RoughSolutionDto(SolutionDto):
#     rough_solution_id: Optional[int]


# @dataclass
# class PrefilledCodeDto(SolutionDto):
#     prefilled_code_id: Optional[int]


# @dataclass
# class CleanSolutionDto(SolutionDto):
#     clean_solution_id: Optional[int]


# @dataclass
# class TestCaseDto:
#     test_case_id: Optional[int]
#     test_case_number: int
#     input: str
#     output: str
#     score: int
#     is_hidden: bool


# @dataclass
# class HintDto:
#     hint_id: Optional[int]
#     hint_number: int
#     title: str
#     description: DescriptionDto

# @dataclass
# class SolutionApproachDto:
#     title: str
#     solution_approach_id: int
#     description_content: str
#     description_content_type: str
#     complexity_analysis_content: str
#     complexity_analysis_content_type: str