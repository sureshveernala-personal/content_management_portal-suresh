from typing import Dict, Optional
from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.dtos.dtos import HintDto, DescriptionDto


class CreateHintInteractor:
    def __init__(
            self,
            hint_storage: HintStorageInterface,
            presenter: PresenterInterface,
            question_storage: QuestionStorageInterface
        ):
        self.hint_storage = hint_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def create_hint(self, question_id: int, hint_details: Dict):
        hint_id = hint_details['hint_id']
        self._validate_question_id(question_id=question_id)
        hint_dto = self._convert_hint_dict_to_hint_dto(
            hint=hint_details
        )
        is_update = hint_id is not None
        updated_hint_dto = self._update_hint_number(
            hint_dto=hint_dto, question_id=question_id
        )
        if is_update:
            self._validate_hint(
                question_id=question_id, hint_id=hint_id
            )
            hint_with_question_id_dto = \
            self.hint_storage.update_hint(
                hint_details=updated_hint_dto
            )
        else:
            hint_with_question_id_dto = \
            self.hint_storage.create_hint(
                question_id=question_id, hint_details=updated_hint_dto
            )

        hint_dict = self.presenter.\
            get_create_hint_response(
                hint_with_question_id_dto=hint_with_question_id_dto,
                question_id=question_id
            )
        return hint_dict


    def _convert_hint_dict_to_hint_dto(self, hint: Dict):
        description = hint['description']
        hint_dto = HintDto(
            hint_id=hint['hint_id'],
            hint_number=hint['hint_number'],
            title=hint['title'],
            content=description['content'],
            content_type=description['content_type']
        )
        return hint_dto


    def _validate_question_id(self, question_id: int):
        is_invalid_question_id = not self.question_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()


    def _validate_hint(self, hint_id: int, question_id: int):
        is_valid_hint_id = self.hint_storage.is_valid_hint_id(
            hint_id=hint_id
        )
        is_invalid_hint_id = not is_valid_hint_id
        if is_invalid_hint_id:
            self.presenter.raise_invalid_hint_id_exception()

        is_hint_not_belongs_to_question = not self.hint_storage.\
            is_hint_belongs_to_question(
                question_id=question_id, hint_id=hint_id
            )
        if is_hint_not_belongs_to_question:
           self.presenter.raise_hint_not_belongs_to_question_exception()


    def _update_hint_number(self, hint_dto: HintDto, question_id:int):
        max_hint_number = self.hint_storage.get_max_hint_number(
            question_id=question_id
        )
        is_first_hint = not max_hint_number
        if is_first_hint:
            hint_dto.hint_number = 1
        else:
            hint_dto.hint_number = max_hint_number + 1
        return hint_dto
