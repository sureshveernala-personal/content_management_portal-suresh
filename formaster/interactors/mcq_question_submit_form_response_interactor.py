from formaster.interactors.base_submit_form_response_interactor import \
    BaseSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.mixins.option_validation_mixin import \
    OptionValidationMixin
from formaster.interactors.storages.dtos import MCQResponseDTO


class MCQQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor, OptionValidationMixin
    ):

    def __init__(
            self, storage: StorageInterface, user_id: int, form_id,
            question_id:int, option_id: int
        ):
        super().__init__(
            storage=storage, user_id=user_id,form_id=form_id,
            question_id=question_id
        )
        self.option_id = option_id


    def _validate_user_response(self):
        self._validate_option_id_with_question(
            option_id=self.option_id, question_id=self.question_id
        )


    def _create_user_response(self):
        mcq_response_dto = MCQResponseDTO(
            user_id=self.user_id,
            question_id=self.question_id,
            option_id=self.option_id
        )
        response_id = self.storage.create_user_mcq_response(
            mcq_response_dto=mcq_response_dto
        )
        return response_id
