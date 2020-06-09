from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface

from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List
from content_management_portal.interactors.storages.dtos \
    import RoughSolutionDto


class CreateRoughSolutionsInteractor:
    def __init__(
            self,
            rough_solution_storage: RoughSolutionStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.rough_solution_storage = rough_solution_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def create_rough_solutions(
            self, question_id: str, rough_solutions: List[Dict]
        ):
        is_invalid_question_id = not self.question_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
            return

        rough_solution_dtos_list = self._get_rough_solutons_dtos_list(
            rough_solutions
        )
        self._update_rough_solutions(
            rough_solution_dtos_list=rough_solution_dtos_list,
            question_id=question_id
        )
        self._create_new_rough_solutions(
            rough_solution_dtos_list=rough_solution_dtos_list,
            question_id=question_id
        )
        new_rough_solution_dtos = self.rough_solution_storage.\
            get_rough_solutions(question_id=question_id)
        question_id_dict = self.presenter.get_create_rough_solutions_response(
            rough_solution_with_question_id_dtos=new_rough_solution_dtos,
            question_id=question_id
        )
        return question_id_dict


    @staticmethod
    def _get_rough_solutons_dtos_list(rough_solutions: List):
        rough_solution_dtos_list = [
            RoughSolutionDto(
                language=solution['language'],
                solution_content=solution['solution_content'],
                file_name=solution['file_name'],
                rough_solution_id=solution['rough_solution_id']
            )
            for solution in rough_solutions
        ]
        return rough_solution_dtos_list


    def _valiadate_rough_solution(
            self, total_rough_solutions: List[int],
            question_rough_solutions: List[int], rough_solution_id: int
        ):
        is_invalid_rough_solution_id = rough_solution_id not in \
            total_rough_solutions
        if is_invalid_rough_solution_id:
            self.presenter.raise_invalid_rough_solution_exception()
            return
        is_not_questions_rough_solution_id = rough_solution_id not in\
            question_rough_solutions
        if is_not_questions_rough_solution_id:
            self.presenter.\
                raise_rough_solution_not_belongs_to_question_exception()
        return


    def _create_new_rough_solutions(
            self,
            rough_solution_dtos_list: List[RoughSolutionDto],
            question_id: int
        ):
        have_to_create_rough_solutions_list = [
            solution_dto
            for solution_dto in rough_solution_dtos_list
            if solution_dto.rough_solution_id is None
        ]

        self.rough_solution_storage.create_rough_solutions(
            question_id=question_id,
            rough_solutions_dtos=have_to_create_rough_solutions_list
        )
        return

    def _update_rough_solutions(
            self, rough_solution_dtos_list: List[RoughSolutionDto],
            question_id: int
        ):
        have_to_update_rough_solutions_list =[]
        have_to_update_rough_solution_ids_list =[]
        for rough_solution_dto in rough_solution_dtos_list:
            is_update = rough_solution_dto.rough_solution_id is not None
            if is_update:
                have_to_update_rough_solution_ids_list.append(
                    rough_solution_dto.rough_solution_id
                )
                have_to_update_rough_solutions_list.append(rough_solution_dto)
        total_rough_solutions = \
            self.rough_solution_storage.get_rough_solution_ids()
        question_rough_solutions = \
            self.rough_solution_storage.get_question_rough_solution_ids(
                question_id=question_id
            )
        for rough_solution_id in have_to_update_rough_solution_ids_list:
            self._valiadate_rough_solution(
                rough_solution_id=rough_solution_id,
                total_rough_solutions=total_rough_solutions,
                question_rough_solutions=question_rough_solutions
            )
        self.rough_solution_storage.update_rough_solutions(
            rough_solution_ids=have_to_update_rough_solution_ids_list,
            rough_solution_dtos=have_to_update_rough_solutions_list
        )
        return
