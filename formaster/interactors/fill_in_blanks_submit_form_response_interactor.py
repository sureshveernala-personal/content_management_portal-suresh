from formaster.interactors.base_submit_form_response_interactor import \
    BaseSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.dtos import FillInBlanksResponseDTO


class FillInBlanksSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor
    ):

    def __init__(
            self, storage: StorageInterface, user_id: int, form_id,
            question_id:int, response_text: int
        ):
        super().__init__(
            storage=storage, user_id=user_id,form_id=form_id,
            question_id=question_id
        )
        self.response_text = response_text


    def _validate_user_response(self):
        pass


    def _create_user_response(self):
        fill_in_blanks_response_dto = FillInBlanksResponseDTO(
            user_id=self.user_id,
            question_id=self.question_id,
            response_text=self.response_text
        )
        response_id = self.storage.create_user_fill_in_blanks_response(
            fill_in_blanks_response_dto=fill_in_blanks_response_dto
        )
        return response_id
