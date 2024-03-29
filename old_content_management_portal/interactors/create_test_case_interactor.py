from typing import Dict, Optional
from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.dtos.dtos import TestCaseDto


class CreateTestCaseInteractor:
    def __init__(
            self,
            test_case_storage: TestCaseStorageInterface,
            presenter: PresenterInterface,
            problem_statement_storage: ProblemStatementStorageInterface
        ):
        self.test_case_storage = test_case_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def create_test_case(self, question_id: int, test_case_details: Dict):
        test_case_id = test_case_details['test_case_id']
        self._validate_question_id(question_id=question_id)
        test_case_dto = self._convert_test_case_dict_to_test_case_dto(
            test_case=test_case_details
        )
        is_update = test_case_id is not None
        if is_update:
            self._validate_test_case(
                question_id=question_id, test_case_id=test_case_id
            )
            test_case_with_question_id_dto = \
            self.test_case_storage.update_test_case(
                test_case_details=test_case_dto
            )
        else:
            test_case_with_question_id_dto = \
            self.test_case_storage.create_test_case(
                question_id=question_id, test_case_details=test_case_dto
            )
        test_case_dict = self.presenter.\
            get_create_test_case_response(
                test_case_with_question_id_dto=test_case_with_question_id_dto
            )
        return test_case_dict

    def _convert_test_case_dict_to_test_case_dto(self, test_case: Dict):
        test_case_dto = TestCaseDto(
            test_case_id=test_case['test_case_id'],
            test_case_number=test_case['test_case_number'],
            input=test_case['input'],
            output=test_case['output'],
            score=test_case['score'],
            is_hidden=test_case['is_hidden']
        )
        return test_case_dto

    def _validate_question_id(self, question_id: int):
        is_invalid_question_id = not self.problem_statement_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

    def _validate_test_case(self, test_case_id: int, question_id: int):
        is_valid_test_case_id = self.test_case_storage.is_valid_test_case_id(
            test_case_id=test_case_id
        )
        is_invalid_test_case_id = not is_valid_test_case_id
        if is_invalid_test_case_id:
            self.presenter.raise_invalid_test_case_id_exception()
        is_test_case_not_belongs_to_question = not self.test_case_storage.\
            is_test_case_belongs_to_question(
                question_id=question_id, test_case_id=test_case_id
            )
        if is_test_case_not_belongs_to_question:
           self.presenter.raise_test_case_not_belongs_to_question_exception()
