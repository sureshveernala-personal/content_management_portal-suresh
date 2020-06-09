from content_management_portal.interactors.storages.\
    prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface


class DeletePrefilledCodeInteractor:
    def __init__(
            self,
            prefilled_code_storage: PrefilledCodeStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.prefilled_code_storage = prefilled_code_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def delete_prefilled_code(self, question_id: int, prefilled_code_id: int):
        self._validating_arguments(
            question_id=question_id, prefilled_code_id=prefilled_code_id
        )
        self.prefilled_code_storage.delete_prefilled_code(
            prefilled_code_id=prefilled_code_id
        )
        return


    def _validating_arguments(self, question_id: int, prefilled_code_id: int):
        is_valid_question_id = self\
            .question_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

        is_valid_prefilled_code_id = \
            self.prefilled_code_storage.is_valid_prefilled_code_id(
                prefilled_code_id=prefilled_code_id
            )
        is_invalid_prefilled_code_id = not is_valid_prefilled_code_id
        if is_invalid_prefilled_code_id:
            self.presenter.raise_invalid_prefilled_code_id_exception()

        is_prefilled_code_belongs_to_question = self.prefilled_code_storage.\
            is_prefilled_code_belongs_to_question(
                question_id=question_id, prefilled_code_id=prefilled_code_id
            )
        is_not_questions_prefilled_code_id = \
            not is_prefilled_code_belongs_to_question
        if is_not_questions_prefilled_code_id:
            self.presenter.\
                raise_prefilled_code_not_belongs_to_question_exception()
