from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List


class GetQuestionsInteractor:
    def __init__(
            self,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.problem_statement_storage = problem_statement_storage
        self.presenter = presenter

    def get_questions(self, offset: int, limit: int):
        if self._is_not_positive(offset):
            self.presenter.raise_invalid_offset_value_exception()
            return
        if self._is_not_positive(limit):
            self.presenter.raise_invalid_limit_value_exception()
            return
        questions_dto = self.problem_statement_storage.get_questions(
            offset=offset, limit=limit
        )
        questions_dict = self.presenter.get_questions_response(
            questions_dto=questions_dto
        )
        return questions_dict

    @staticmethod
    def _is_not_positive(number: int) -> bool:
        is_not_positive = number <= 0
        return is_not_positive
