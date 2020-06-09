from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.\
    presenter_interface import PresenterInterface
from content_management_portal.interactors.storages.dtos import \
    HintsSwapDetailsDto
from typing import Dict, List


class SwapHintsInteractor:

    def __init__(
            self,
            hint_storage: HintStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.hint_storage = hint_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def swap_hints(
            self, question_id: int, hints_swap_details: Dict
        ):
        self._validating_arguments(
            question_id=question_id,
            hints_swap_details=hints_swap_details
        )
        hint_dto = self._get_hint_id_and_number_dto(
                hint_dict=hints_swap_details
            )
        temp = hint_dto.first_hint_number
        hint_dto.first_hint_number = \
            hint_dto.second_hint_number
        hint_dto.second_hint_number = temp
        self.hint_storage.swap_hints(
            hints_swap_details=hint_dto
        )
        return


    def _validating_arguments(
            self, question_id: int, hints_swap_details: Dict
        ):
        is_valid_question_id = self\
            .question_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

        total_hint_ids = self.hint_storage.get_hint_ids()
        total_question_hint_ids = self.hint_storage.\
            get_given_question_hint_ids(question_id=question_id)
        for hint in hints_swap_details:
            hint_id = hints_swap_details[hint]['hint_id']
            self._validating_hint_id(
                question_id=question_id, hint_id=hint_id,
                total_hint_ids=total_hint_ids,
                total_question_hint_ids=total_question_hint_ids
            )


    def _validating_hint_id(
            self,
            hint_id: int, question_id:int,
            total_hint_ids: List[int],
            total_question_hint_ids: List[int]
        ):
        is_invalid_first_hint_id = hint_id not in total_hint_ids
        if is_invalid_first_hint_id:
            self.presenter.raise_invalid_hint_id_exception()
            return

        is_hint_not_belongs_to_question = \
            hint_id not in total_question_hint_ids
        if is_hint_not_belongs_to_question:
            self.presenter.raise_hint_not_belongs_to_question_exception()


    @staticmethod
    def _get_hint_id_and_number_dto(hint_dict: Dict):
        first_hint_dict = hint_dict['first_hint']
        second_hint_dict = hint_dict['second_hint']
        hint_id_and_number_dto = HintsSwapDetailsDto(
            first_hint_id=first_hint_dict['hint_id'],
            first_hint_number=first_hint_dict['hint_number'],
            second_hint_id=second_hint_dict['hint_id'],
            second_hint_number=second_hint_dict['hint_number']
        )
        return hint_id_and_number_dto
