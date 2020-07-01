from abc import ABC
from abc import abstractmethod
from content_management_portal.dtos.dtos import DescriptionDto
from content_management_portal.interactors.storages.dtos \
    import QuestionStatusDto, QuestionDto
from typing import Tuple, List


class QuestionStorageInterface(ABC):

    @abstractmethod
    def is_valid_question_id(self, question_id) -> bool:
        pass


    @abstractmethod
    def create_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: DescriptionDto
        ) -> QuestionDto:
        pass


    @abstractmethod
    def update_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: DescriptionDto,
            question_id: int
        ) -> int:
        pass


    @abstractmethod
    def get_questions(
            self, from_value: int, to_value: int
        ) -> QuestionStatusDto:
        pass


    @abstractmethod
    def get_question_details(self, question_id: int) -> Tuple:
        pass


    @abstractmethod
    def get_total_number_of_questions(self) -> int:
        pass


    @abstractmethod
    def get_all_question_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_question_user_id(self, question_id: int) -> int:
        pass
