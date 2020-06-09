from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import \
    PrefilledCodeDto, PrefilledCodeWithQuestionIdDto


class PrefilledCodeStorageInterface(ABC):

    @abstractmethod
    def create_prefilled_codes(
            self,
            question_id: int,
            prefilled_code_dtos: List[PrefilledCodeDto]
        ):
        pass


    @abstractmethod
    def is_valid_prefilled_code_id(self, prefilled_code_id: int) -> bool:
        pass


    @abstractmethod
    def is_prefilled_code_belongs_to_question(
            self, question_id: int, prefilled_code_id: int
        ) -> bool:
        pass


    @abstractmethod
    def get_prefilled_code_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_question_prefilled_code_ids(self, question_id: int) -> List[int]:
        pass


    @abstractmethod
    def update_prefilled_codes(
            self,
            prefilled_code_ids: List[int],
            prefilled_code_dtos: List[PrefilledCodeDto]
        ) -> None:
        pass


    @abstractmethod
    def get_prefilled_codes(
            self, question_id: int
        ) -> PrefilledCodeWithQuestionIdDto:
        pass


    @abstractmethod
    def delete_prefilled_code(self, prefilled_code_id: int) -> None:
        pass
