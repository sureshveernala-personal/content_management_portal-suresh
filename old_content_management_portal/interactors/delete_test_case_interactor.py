from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface


class DeleteTestCaseInteractor:
    def __init__(
            self,
            test_case_storage: TestCaseStorageInterface,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.test_case_storage = test_case_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def delete_test_case(self, question_id: int, test_case_id: int):
        self._validating_arguments(
            question_id=question_id, test_case_id=test_case_id
        )
        self.test_case_storage.delete_test_case(
            question_id=question_id, test_case_id=test_case_id
        )
        return

    def _validating_arguments(self, question_id: int, test_case_id: int):
        is_valid_question_id = self\
            .problem_statement_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
        is_valid_test_case_id = \
            self.test_case_storage.is_valid_test_case_id(
                test_case_id=test_case_id
            )
        is_invalid_test_case_id = not is_valid_test_case_id
        if is_invalid_test_case_id:
            self.presenter.raise_invalid_test_case_id_exception()
        is_test_case_belongs_to_question = self.test_case_storage.\
            is_test_case_belongs_to_question(
                question_id=question_id, test_case_id=test_case_id
            )
        is_test_case_not_belongs_to_question = \
            not is_test_case_belongs_to_question
        if is_test_case_not_belongs_to_question:
            self.presenter.raise_test_case_not_belongs_to_question_exception()
