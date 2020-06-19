from abc import ABC, abstractmethod
from formaster.interactors.storages.dtos import FormDto, MCQResponseDTO,\
    FillInBlanksResponseDTO


class StorageInterface(ABC):

    @abstractmethod
    def get_form(self, form_id: int) -> FormDto:
        pass


    @abstractmethod
    def is_valid_option_id(self, option_id: int) -> bool:
        pass


    @abstractmethod
    def is_option_id_belongs_to_question(
            self, question_id: int, option_id: int
        ) -> bool:
        pass


    @abstractmethod
    def is_valid_question_id(self, question_id: int) -> bool:
        pass


    @abstractmethod
    def is_question_id_belongs_form(
            self, form_id: int, question_id: int
        ) -> bool:
        pass

    @abstractmethod
    def create_user_mcq_response(self, mcq_response_dto: MCQResponseDTO) -> int:
        pass

    @abstractmethod
    def create_user_fill_in_blanks_response(
            self, fill_in_blanks_response_dto: FillInBlanksResponseDTO
        ) -> int:
        pass
