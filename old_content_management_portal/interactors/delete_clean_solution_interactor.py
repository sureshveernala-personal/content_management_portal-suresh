from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface


class DeleteCleanSolutionInteractor:
    def __init__(
            self,
            clean_solution_storage: CleanSolutionStorageInterface,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.clean_solution_storage = clean_solution_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def delete_clean_solution(self, question_id: int, clean_solution_id: int):
        self._validating_arguments(
            question_id=question_id, clean_solution_id=clean_solution_id
        )
        self.clean_solution_storage.delete_clean_solution(
            clean_solution_id=clean_solution_id
        )
        return

    def _validating_arguments(self, question_id: int, clean_solution_id: int):
        is_valid_question_id = self\
            .problem_statement_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
        is_valid_clean_solution_id = \
            self.clean_solution_storage.is_valid_clean_solution_id(
                clean_solution_id=clean_solution_id
            )
        is_invalid_clean_solution_id = not is_valid_clean_solution_id
        if is_invalid_clean_solution_id:
            self.presenter.raise_invalid_clean_solution_id_exception()
        is_clean_solution_belongs_to_question = self.clean_solution_storage.\
            is_clean_solution_belongs_to_question(
                question_id=question_id, clean_solution_id=clean_solution_id
            )
        is_not_questions_clean_solution_id = \
            not is_clean_solution_belongs_to_question
        if is_not_questions_clean_solution_id:
            self.presenter.\
                raise_clean_solution_not_belongs_to_question_exception()
