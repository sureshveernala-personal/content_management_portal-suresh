from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List
from content_management_portal.dtos.dtos import SolutionDto


class CreateCleanSolutionsInteractor:
    def __init__(
            self,
            question_storage: QuestionStorageInterface,
            question_id:int,
            solution_dtos: List[SolutionDto],
            clean_solution_storage:  CleanSolutionStorageInterface
        ):
        super().__init__(
            question_storage=question_storage,
            question_id=question_id,
            solution_dtos=solution_dtos,
        )
        self.clean_solution_storage = clean_solution_storage


    def _get_question_solution_ids(self):
        question_clean_solutions = \
            self.clean_solution_storage.get_question_clean_solution_ids(
                question_id=self.question_id
            )
        return question_clean_solutions


    def _get_total_solution_ids(self):
        total_clean_solutions = \
            self.clean_solution_storage.get_clean_solution_ids()
        return total_clean_solutions


    def _create_new_solutions(self, solution_dtos: List[SolutionDto]):
        self.clean_solution_storage.create_clean_solutions(
            question_id=self.question_id,
            clean_solution_dtos=solution_dtos
        )


    def _update_solutions(
            self, solution_ids: List[int], solution_dtos: List[SolutionDto]
        ):
        self.clean_solution_storage.update_clean_solutions(
            clean_solution_ids= solution_ids,
            clean_solution_dtos=solution_dtos
        )


    def _get_solutions(self):
        clean_solution_dtos = self.clean_solution_storage.\
            get_clean_solutions(question_id=self.question_id)
        return clean_solution_dtos
