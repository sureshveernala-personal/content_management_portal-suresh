from typing import Dict, Optional
from content_management_portal.interactors.storages.\
    solution_approach_storage_interface import SolutionApproachStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.interactors.storages.dtos import SolutionApproachDto


class CreateSolutionApproachInteractor:
    def __init__(
            self,
            solution_approach_storage: SolutionApproachStorageInterface,
            presenter: PresenterInterface,
            problem_statement_storage: ProblemStatementStorageInterface
        ):
        self.solution_approach_storage = solution_approach_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def create_solution_approach(self, question_id: int, solution_approach_details: Dict):
        solution_approach_id = solution_approach_details['solution_approach_id']
        self._validate_question_id(question_id=question_id)
        solution_approach_dto = self._convert_solution_approach_dict_to_solution_approach_dto(
            solution_approach=solution_approach_details
        )
        is_update = solution_approach_id is not None
        if is_update:
            self._validate_solution_approach(
                question_id=question_id, solution_approach_id=solution_approach_id
            )
            response_solution_approach_dto = \
            self.solution_approach_storage.update_solution_approach(
                solution_approach_details=solution_approach_dto
            )
        else:
            response_solution_approach_dto = \
            self.solution_approach_storage.create_solution_approach(
                question_id=question_id,
                solution_approach_details=solution_approach_dto
            )
        solution_approach_dict = self.presenter.\
            get_create_solution_approach_response(question_id=question_id, 
                solution_approach_dto=response_solution_approach_dto
            )
        return solution_approach_dict

    def _convert_solution_approach_dict_to_solution_approach_dto(
            self, solution_approach: Dict
        ):
        description = solution_approach['description']
        complexity_analysis = solution_approach['complexity_analysis']
        solution_approach_dto = SolutionApproachDto(
            solution_approach_id=solution_approach['solution_approach_id'],
            title=solution_approach['title'],
            description_content=description['content'],
            description_content_type=description['content_type'],
            complexity_analysis_content=complexity_analysis['content'],
            complexity_analysis_content_type=complexity_analysis['content_type']
        )
        return solution_approach_dto

    def _validate_question_id(self, question_id: int):
        is_invalid_question_id = not self.problem_statement_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()

    def _validate_solution_approach(self, solution_approach_id: int, question_id: int):
        is_valid_solution_approach_id = \
            self.solution_approach_storage.is_valid_solution_approach_id(
                solution_approach_id=solution_approach_id
            )
        is_invalid_solution_approach_id = not is_valid_solution_approach_id
        if is_invalid_solution_approach_id:
            self.presenter.raise_invalid_solution_approach_id_exception()
        is_solution_approach_not_belongs_to_question = \
            not self.solution_approach_storage.\
                is_solution_approach_belongs_to_question(
                    question_id=question_id,
                    solution_approach_id=solution_approach_id
                )
        if is_solution_approach_not_belongs_to_question:
           self.presenter.\
               raise_solution_approach_not_belongs_to_question_exception()
