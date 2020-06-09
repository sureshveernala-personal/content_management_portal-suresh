from abc import ABC
from abc import abstractmethod
from content_management_portal.interactors.storages.dtos import \
    HintDto, HintWithQuestionIdDto, HintsSwapDetailsDto
import pytest
from typing import List


class HintStorageInterface(ABC):

    @abstractmethod
    def create_hint(
            self, question_id: int, hint_details: HintDto
        ) -> HintWithQuestionIdDto:
        pass


    @abstractmethod
    def update_hint(self, hint_details: HintDto) -> HintWithQuestionIdDto:
        pass


    @abstractmethod
    def is_valid_hint_id(self, hint_id: int) -> bool:
        pass


    @abstractmethod
    def is_hint_belongs_to_question(
            self, question_id: int, hint_id: int
        ) -> bool:
        pass


    @abstractmethod
    def delete_hint(self, question_id: int, hint_id: int) -> int:
        pass


    @abstractmethod
    def decrease_hint_numbers_followed_given_hint_number(
            self, question_id: int, hint_number: int
        ):
        pass


    @abstractmethod
    def swap_hints(
            self, hints_swap_details: HintsSwapDetailsDto
        ):
        pass


    @abstractmethod
    def get_hint_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_given_question_hint_ids(self, question_id: int) -> List[int]:
        pass


    @abstractmethod
    def get_max_hint_number(self, question_id: int):
        pass
