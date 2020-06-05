from abc import ABC
from abc import abstractmethod
from content_management_portal.interactors.storages.dtos import TestCaseDto,\
    TestCaseWithQuestionIdDto, TestCasesSwapDetailsDto
import pytest
from typing import List


class TestCaseStorageInterface(ABC):

    @abstractmethod
    def create_test_case(
            self, question_id: int, test_case_details: TestCaseDto
        ) -> TestCaseWithQuestionIdDto:
        pass

    @abstractmethod
    def update_test_case(
            self, test_case_details: TestCaseDto
        ) -> TestCaseWithQuestionIdDto:
        pass

    @abstractmethod
    def is_valid_test_case_id(self, test_case_id: int) -> bool:
        pass

    @abstractmethod
    def is_test_case_belongs_to_question(
            self, question_id: int, test_case_id: int
        ) -> bool:
        pass

    @abstractmethod
    def delete_test_case(self, question_id: int, test_case_id: int):
        pass

    @abstractmethod
    def swap_test_cases(
            self, test_cases_swap_details: TestCasesSwapDetailsDto
        ):
        pass

    @abstractmethod
    def get_test_case_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_given_question_test_case_ids(self, question_id: int) -> List[int]:
        pass
