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
from content_management_portal.exceptions.exceptions import InvalidQuestionId,\
    InvalidSolutionIds, SolutionIdsNotBelongsToQuestion


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
        except InvalidSolutionIds:
            presenter.raise_invalid_solution_id_exception()
        except SolutionIdsNotBelongsToQuestion:
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
        self._validate_question_id(question_id=self.question_id)

        have_to_update_solutions, have_to_update_solution_ids = \
            self._get_updating_list()

        self._valiadate_solutions(solution_ids=have_to_update_solution_ids)

        self._update_solutions(
            solution_ids=have_to_update_solution_ids,
            solution_dtos=have_to_update_solutions
        )

        have_to_create_solutions_list = \
            self._get_have_to_create_solutions_list()
        self._create_new_solutions(solution_dtos=have_to_create_solutions_list)

        new_solution_dtos = self._get_solutions()

        return new_solution_dtos


    def _get_updating_list(self):
        have_to_update_solutions =[]
        have_to_update_solution_ids =[]
        for solution_dto in self.solution_dtos:
            is_update = solution_dto.id is not None
            if is_update:
                have_to_update_solution_ids.append(solution_dto.solution_id)
                have_to_update_solutions.append(solution_dto)
        return have_to_update_solutions, have_to_update_solution_ids


    def _get_have_to_create_solutions_list(self):
        have_to_create_solutions_list = [
            solution_dto
            for solution_dto in self.solution_dtos
            if solution_dto.id is None
        ]
        return have_to_create_solutions_list


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


    def _valiadate_solutions(self, solution_ids: List[int]):
        invalid_solution_ids = \
            self._invalid_solution_ids(solution_ids=solution_ids)
        if invalid_solution_ids:
            raise InvalidSolutionIds(solution_ids=solution_ids)

        solution_ids_not_in_question = self._solution_ids_not_in_question(
            solution_ids=solution_ids
        )
        if solution_ids_not_in_question:
            raise SolutionIdsNotBelongsToQuestion(
                solution_ids=solution_ids_not_in_question
            )


    def _invalid_solution_ids(self, solution_ids: List[int]):
        total_solution_ids = self._get_total_solution_ids()
        invalid_solution_ids = [
            solution_id
            for solution_id in solution_ids
            if solution_id not in total_solution_ids
        ]
        return invalid_solution_ids


    def _solution_ids_not_in_question(self, solution_ids: List[int]):
        question_solution_ids = self._get_question_solution_ids()

        solution_ids_not_in_question = [
            solution_id
            for solution_id in solution_ids
            if solution_id not in question_solution_ids
        ]
        return solution_ids_not_in_question


    @abstractmethod
    def _get_question_solution_ids(self):
        pass


    @abstractmethod
    def _get_total_solution_ids(self):
        pass


    @abstractmethod
    def _create_new_solutions(self, solution_dtos: List[SolutionDto]):
        pass


    @abstractmethod
    def _update_solutions(
            self, solution_ids: List[int], solution_dtos: List[SolutionDto]
        ):
        pass


    @abstractmethod
    def _get_solutions(self):
        pass
