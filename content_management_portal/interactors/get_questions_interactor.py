from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List


class GetQuestionsInteractor:

    def __init__(
            self,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.question_storage = question_storage
        self.presenter = presenter

    def get_questions(self, offset: int, limit: int):
        if self._is_not_positive(offset):
            self.presenter.raise_invalid_offset_value_exception()
            return

        if self._is_not_positive(limit):
            self.presenter.raise_invalid_limit_value_exception()
            return

        total_questions = self.question_storage.\
            get_total_number_of_questions()
        from_value = offset-1
        to_value = from_value + limit
        if from_value >= total_questions:
            from_value = 0
            to_value = 0

        question_status_dtos = self.question_storage.get_questions(
            from_value=from_value, to_value=to_value
        )
        questions_dict = self.presenter.get_questions_response(
            question_status_dtos=question_status_dtos,
            total_questions=total_questions,
            offset=offset, limit=limit
        )
        return questions_dict


    @staticmethod
    def _is_not_positive(number: int) -> bool:
        is_not_positive = number <= 0
        return is_not_positive
