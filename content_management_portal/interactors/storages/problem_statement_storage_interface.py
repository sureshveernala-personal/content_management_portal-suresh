from abc import ABC
from abc import abstractmethod
from content_management_portal.dtos.dtos import DescriptionDto
from content_management_portal.interactors.storages.dtos import \
    QuestionsDto, QuestionDto

class ProblemStatementStorageInterface(ABC):

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
    def delete_problem_statement(
            self,
            question_id: int
        ) -> None:
        pass

    @abstractmethod
    def get_questions(self, offset: int, limit: int) -> QuestionsDto:
        pass

    @abstractmethod
    def get_question_details(self, question_id: int):
        pass
