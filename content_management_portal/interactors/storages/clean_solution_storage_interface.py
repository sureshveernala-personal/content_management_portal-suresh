from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import \
    CleanSolutionDto, CleanSolutionWithQuestionIdDto


class CleanSolutionStorageInterface(ABC):

    @abstractmethod
    def create_clean_solutions(
            self,
            question_id: int,
            clean_solution_dtos: List[CleanSolutionDto]
        ):
        pass


    @abstractmethod
    def is_valid_clean_solution_id(self, clean_solution_id: int) -> bool:
        pass


    @abstractmethod
    def is_clean_solution_belongs_to_question(
            self, question_id: int, clean_solution_id: int
        ) -> bool:
        pass


    @abstractmethod
    def get_clean_solution_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_question_clean_solution_ids(self, question_id: int) -> List[int]:
        pass


    @abstractmethod
    def update_clean_solutions(
            self,
            clean_solution_ids: List[int],
            clean_solution_dtos: List[CleanSolutionDto]
        ) -> None:
        pass


    @abstractmethod
    def get_clean_solutions(
            self, question_id: int
        ) -> CleanSolutionWithQuestionIdDto:
        pass


    @abstractmethod
    def delete_clean_solution(self, clean_solution_id: int) -> None:
        pass
