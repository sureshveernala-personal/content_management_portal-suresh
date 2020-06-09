from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionDto, RoughSolutionWithQuestionIdDto


class RoughSolutionStorageInterface(ABC):

    @abstractmethod
    def create_rough_solutions(
            self,
            question_id: int,
            rough_solutions_dtos: List[RoughSolutionDto]
        ) -> None:
        pass


    @abstractmethod
    def is_valid_rough_solution_id(self, rough_solution_id: int) -> bool:
        pass


    @abstractmethod
    def is_rough_solution_belongs_to_question(
            self, question_id: int, rough_solution_id: int
        ) -> bool:
        pass


    @abstractmethod
    def get_rough_solution_ids(self) -> List[int]:
        pass


    @abstractmethod
    def get_question_rough_solution_ids(self, question_id: int) -> List[int]:
        pass


    @abstractmethod
    def update_rough_solutions(
            self,
            rough_solution_ids: List[int],
            rough_solution_dtos: List[RoughSolutionDto]
        ) -> None:
        pass


    @abstractmethod
    def get_rough_solutions(
            self, question_id: int
        ) -> List[RoughSolutionWithQuestionIdDto]:
        pass


    @abstractmethod
    def delete_rough_solution(self, rough_solution_id: int) -> None:
        pass
