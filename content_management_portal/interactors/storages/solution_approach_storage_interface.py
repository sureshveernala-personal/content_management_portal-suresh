from abc import ABC
from abc import abstractmethod
from content_management_portal.interactors.storages.dtos import \
    SolutionApproachDto

class SolutionApproachStorageInterface(ABC):

    @abstractmethod
    def create_solution_approach(
            self, question_id: int,
            solution_approach_details: SolutionApproachDto
        ) -> int:
        pass


    @abstractmethod
    def update_solution_approach(
            self, solution_approach_details: SolutionApproachDto
        ) -> int:
        pass


    @abstractmethod
    def is_valid_solution_approach_id(self, solution_approach_id: int):
        pass


    @abstractmethod
    def is_solution_approach_belongs_to_question(
            self, question_id: int, solution_approach_id: int
        ):
        pass
