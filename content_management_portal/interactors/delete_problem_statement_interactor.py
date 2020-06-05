from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface

class DeleteProblemStatementInteractor:
    def __init__(
            self,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.problem_statement_storage = problem_statement_storage
        self.presenter = presenter

    def delete_problem_statement(self, question_id: int):
        is_valid_question_id = \
            self.problem_statement_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

        self.problem_statement_storage.delete_problem_statement(
            question_id=question_id
        )
        return
