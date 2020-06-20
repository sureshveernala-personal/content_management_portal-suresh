from abc import abstractmethod
from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List
from content_management_portal.dtos.dtos import SolutionDto
from content_management_portal.interactors.mixins.question_validation_mixin\
    import QuestionValidationMixin
from content_management_portal.exceptions.exceptions import InvalidQuestionId


class CreateSolutionsInteractor(QuestionValidationMixin):
    def __init__(
            self, question_storage: QuestionStorageInterface, question_id:int,
            solution_dtos: List[SolutionDto]
        ):
        self.question_storage = question_storage
        self.question_id = question_id
        self.solution_dtos = solution_dtos

    def create_solutions_wrapper(self, presenter: PresenterInterface):
        try:
            new_solution_dtos = \
                self._prepare_solution_response(presenter=presenter)
        except InvalidQuestionId:
            presenter.raise_invalid_question_id_exception()
        except InvalidSolutionId:
            presenter.raise_invalid_solution_id_exception()
        except SolutionNotBelongsToQuestion:
            presenter.raise_solution_not_belongs_to_question_exception()


        solution_dict = presenter.get_create_solutions_response(
            solution_with_question_id_dtos=new_solution_dtos,
            question_id=self.question_id
        )
        return solution_dict
    
    def _prepare_solution_response(self, presenter: PresenterInterface):
        new_solution_dtos = self.create_solutions()

        solution_dict = presenter.get_create_solutions_response(
            solution_with_question_id_dtos=new_solution_dtos,
            question_id=self.question_id
        )
        return solution_dict


    def create_solutions(self):
        self._validate_question_id(question_id=question_id)

        self._update_solutions(question_id=question_id)
        self._create_new_solutions(question_id=question_id)
        new_solution_dtos = self._get_solutions(question_id=question_id)

        return new_solution_dtos


    @abstractmethod
    def _get_solutions(self, question_id: int):
        pass


    # @staticmethod
    # def _get_solutions_dtos_list(solutions: List):
    #     solution_dtos = [
    #         CleanSolutionDto(
    #             language=solution['language'],
    #             solution_content=solution['solution_content'],
    #             file_name=solution['file_name'],
    #             solution_id=solution['solution_id']
    #         )
    #         for solution in solutions
    #     ]
    #     return solution_dtos


    def _valiadate_solutions(
            self, solution_ids: List[int], solution_id: int, question_id: int
        ):
        invalid_solution_ids = \
            self._invalid_solution_ids(solution_ids=solution_ids)
        if invalid_solution_ids:
            raise InvalidSolutionId(solution_ids=solution_ids)

        solution_ids_not_in_question = self._solution_ids_not_in_question(
            solution_ids=solution_ids, question_id=question_id
        )
        if solution_ids_not_in_question:
            raise SolutionNotBelongsToQuestion(
                solution_ids=solution_ids_not_question
            )

    def _create_new_solutions(self, question_id: int):
        have_to_create_solutions_list = [
            solution_dto
            for solution_dto in solution_dtos
            if solution_dto.id is None
        ]

        self.solution_storage.create_solutions(
            question_id=question_id,
            solution_dtos=have_to_create_solutions_list
        )
        return


    def _update_solutions(self, solution_dtos: List, question_id: int):
        have_to_update_solutions =[]
        have_to_update_solution_ids =[]
        for solution_dto in solution_dtos:
            is_update = solution_dto.id is not None
            if is_update:
                have_to_update_solution_ids.append(
                    solution_dto.solution_id
                )
                have_to_update_solutions.append(solution_dto)

        self._valiadate_solutions(
            solution_id=solution_id,
            solution_ids=have_to_update_solution_ids,
        )
        self.solution_storage.update_solutions(
            solution_ids=have_to_update_solution_ids,
            solution_dtos=have_to_update_solutions
        )
        return


    def _invalid_solution_ids(self, solution_ids: List[int]):
        total_solution_ids = self._get_solution_ids()
        invalid_solution_ids = [
            solution_id
            for solution_id in solution_ids
            if solution_id not in total_solution_ids
        ]
        return invalid_solution_ids


    @abstractmethod
    def _get_total_solution_ids(self):
        pass


    def _solution_ids_not_in_question(
            self, solution_ids: List[int], question_id: int
        ):
        question_solution_ids = \
            self._get_question_solution_ids(question_id=question_id)
    
        solution_ids_not_in_question = [
            solution_id
            for solution_id in solution_ids
            if solution_id not in question_solution_ids
        ]
        return solution_ids_not_in_question
    
    
    @abstractmethod
    def _get_question_solution_ids(self, question_id):
        pass
