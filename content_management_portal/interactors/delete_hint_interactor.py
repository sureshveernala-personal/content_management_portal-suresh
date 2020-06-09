from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface


class DeleteHintInteractor:
    def __init__(
            self,
            hint_storage: HintStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.hint_storage = hint_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def delete_hint(self, question_id: int, hint_id: int):
        self._validating_arguments(
            question_id=question_id, hint_id=hint_id
        )
        hint_number = self.hint_storage.delete_hint(
            question_id=question_id, hint_id=hint_id
        )
        self.hint_storage.\
            decrease_hint_numbers_followed_given_hint_number(
                question_id=question_id, hint_number=hint_number
            )
        return


    def _validating_arguments(self, question_id: int, hint_id: int):
        is_valid_question_id = self\
            .question_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
        is_valid_hint_id = \
            self.hint_storage.is_valid_hint_id(
                hint_id=hint_id
            )
        is_invalid_hint_id = not is_valid_hint_id
        if is_invalid_hint_id:
            self.presenter.raise_invalid_hint_id_exception()

        is_hint_belongs_to_question = self.hint_storage.\
            is_hint_belongs_to_question(
                question_id=question_id, hint_id=hint_id
            )
        is_hint_not_belongs_to_question = \
            not is_hint_belongs_to_question
        if is_hint_not_belongs_to_question:
            self.presenter.raise_hint_not_belongs_to_question_exception()
