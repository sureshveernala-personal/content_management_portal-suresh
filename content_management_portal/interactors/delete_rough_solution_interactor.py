from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface


class DeleteRoughSolutionInteractor:
    def __init__(
            self,
            rough_solution_storage: RoughSolutionStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.rough_solution_storage = rough_solution_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def delete_rough_solution(self, question_id: int, rough_solution_id: int):
        self._validating_arguments(
            question_id=question_id, rough_solution_id=rough_solution_id
        )
        self.rough_solution_storage.delete_rough_solution(
            rough_solution_id=rough_solution_id
        )
        return


    def _validating_arguments(self, question_id: int, rough_solution_id: int):
        is_valid_question_id = self\
            .question_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

        is_valid_rough_solution_id = \
            self.rough_solution_storage.is_valid_rough_solution_id(
                rough_solution_id=rough_solution_id
            )
        is_invalid_rough_solution_id = not is_valid_rough_solution_id
        if is_invalid_rough_solution_id:
            self.presenter.raise_invalid_rough_solution_exception()

        is_rough_solution_belongs_to_question = self.rough_solution_storage.\
            is_rough_solution_belongs_to_question(
                question_id=question_id, rough_solution_id=rough_solution_id
            )
        is_not_questions_rough_solution_id = \
            not is_rough_solution_belongs_to_question
        if is_not_questions_rough_solution_id:
            self.presenter.\
                raise_rough_solution_not_belongs_to_question_exception()
