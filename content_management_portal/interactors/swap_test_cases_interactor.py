from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.dtos import \
    TestCasesSwapDetailsDto, TestCaseIdAndNumberDto
from typing import Dict, List


class SwapTestCasesInteractor:
    def __init__(
            self,
            test_case_storage: TestCaseStorageInterface,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.test_case_storage = test_case_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def swap_test_cases(
            self, question_id: int, test_cases_swap_details: Dict
        ):
        self._validating_arguments(
            question_id=question_id,
            test_cases_swap_details=test_cases_swap_details
        )
        first_test_case_dict = test_cases_swap_details['first_test_case']
        second_test_case_dict = test_cases_swap_details['second_test_case']
        first_test_case_dto = self._get_test_case_id_and_number_dto(
                test_case_dict=first_test_case_dict
            )
        second_test_case_dto = self._get_test_case_id_and_number_dto(
                test_case_dict=second_test_case_dict
            )
        temp = first_test_case_dto.test_case_number
        first_test_case_dto.test_case_number = second_test_case_dto.test_case_number
        second_test_case_dto.test_case_number = temp
        test_cases_swap_details_dto = TestCasesSwapDetailsDto(
            first_test_case=first_test_case_dto,
            second_test_case=second_test_case_dto
        )
        self.test_case_storage.swap_test_cases(
            test_cases_swap_details=test_cases_swap_details_dto
        )
        return

    def _validating_arguments(
            self, question_id: int, test_cases_swap_details: Dict
        ):
        is_valid_question_id = self\
            .problem_statement_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
        total_test_case_ids = self.test_case_storage.get_test_case_ids()
        total_question_test_case_ids = self.test_case_storage.\
            get_given_question_test_case_ids(question_id=question_id)
        for test_case in test_cases_swap_details:
            test_case_id = test_cases_swap_details[test_case]['test_case_id']
            self._validating_test_case_id(
                question_id=question_id, test_case_id=test_case_id,
                total_test_case_ids=total_test_case_ids,
                total_question_test_case_ids=total_question_test_case_ids
            )


    def _validating_test_case_id(
            self,
            test_case_id: int, question_id:int,
            total_test_case_ids: List[int],
            total_question_test_case_ids: List[int]
        ):
        is_invalid_first_test_case_id = test_case_id not in total_test_case_ids
        if is_invalid_first_test_case_id:
            self.presenter.raise_invalid_test_case_id_exception()
            return
        is_test_case_not_belongs_to_question = \
            test_case_id not in total_question_test_case_ids
        if is_test_case_not_belongs_to_question:
            self.presenter.raise_test_case_not_belongs_to_question_exception()

    @staticmethod
    def _get_test_case_id_and_number_dto(test_case_dict: Dict):
        test_case_id_and_number_dto = TestCaseIdAndNumberDto(
            test_case_id=test_case_dict['test_case_id'],
            test_case_number=test_case_dict['test_case_number']
        )
        return test_case_id_and_number_dto
