from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List
from content_management_portal.dtos.dtos import CleanSolutionDto


class CreateCleanSolutionsInteractor:
    def __init__(
            self,
            clean_solution_storage: CleanSolutionStorageInterface,
            question_storage: QuestionStorageInterface,
            presenter: PresenterInterface
        ):
        self.clean_solution_storage = clean_solution_storage
        self.presenter = presenter
        self.question_storage = question_storage


    def create_clean_solutions(
            self, question_id: str, clean_solutions: List[Dict]
        ):
        is_invalid_question_id = not self.question_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
            return

        clean_solution_dtos_list = self._get_clean_solutions_dtos_list(
            clean_solutions
        )
        self._update_clean_solutions(
            clean_solution_dtos_list=clean_solution_dtos_list,
            question_id=question_id
        )
        self._create_new_clean_solutions(
            clean_solution_dtos_list=clean_solution_dtos_list,
            question_id=question_id
        )
        new_clean_solution_dtos = self.clean_solution_storage.\
            get_clean_solutions(question_id=question_id)
        question_id_dict = self.presenter.get_create_clean_solutions_response(
            clean_solution_with_question_id_dtos=new_clean_solution_dtos,
            question_id=question_id
        )
        return question_id_dict


    @staticmethod
    def _get_clean_solutions_dtos_list(clean_solutions: List):
        clean_solution_dtos_list = [
            CleanSolutionDto(
                language=solution['language'],
                solution_content=solution['solution_content'],
                file_name=solution['file_name'],
                clean_solution_id=solution['clean_solution_id']
            )
            for solution in clean_solutions
        ]
        return clean_solution_dtos_list


    def _valiadate_clean_solution(
            self, total_clean_solutions: List[int],
            question_clean_solutions: List[int], clean_solution_id: int
        ):
        is_invalid_clean_solution_id = clean_solution_id not in \
            total_clean_solutions
        if is_invalid_clean_solution_id:
            self.presenter.raise_invalid_clean_solution_id_exception()
            return

        is_not_questions_clean_solution_id = clean_solution_id not in\
            question_clean_solutions
        if is_not_questions_clean_solution_id:
            self.presenter.\
                raise_clean_solution_not_belongs_to_question_exception()
        return


    def _create_new_clean_solutions(
            self,
            clean_solution_dtos_list: List[CleanSolutionDto],
            question_id: int
        ):
        have_to_create_clean_solutions_list = [
            solution_dto
            for solution_dto in clean_solution_dtos_list
            if solution_dto.clean_solution_id is None
        ]

        self.clean_solution_storage.create_clean_solutions(
            question_id=question_id,
            clean_solution_dtos=have_to_create_clean_solutions_list
        )
        return


    def _update_clean_solutions(
            self, clean_solution_dtos_list: List[CleanSolutionDto],
            question_id: int
        ):
        have_to_update_clean_solutions_list =[]
        have_to_update_clean_solution_ids_list =[]
        for clean_solution_dto in clean_solution_dtos_list:
            is_update = clean_solution_dto.clean_solution_id is not None
            if is_update:
                have_to_update_clean_solution_ids_list.append(
                    clean_solution_dto.clean_solution_id
                )
                have_to_update_clean_solutions_list.append(clean_solution_dto)

        total_clean_solutions = \
            self.clean_solution_storage.get_clean_solution_ids()
        question_clean_solutions = \
            self.clean_solution_storage.get_question_clean_solution_ids(
                question_id=question_id
            )
        for clean_solution_id in have_to_update_clean_solution_ids_list:
            self._valiadate_clean_solution(
                clean_solution_id=clean_solution_id,
                total_clean_solutions=total_clean_solutions,
                question_clean_solutions=question_clean_solutions
            )
        self.clean_solution_storage.update_clean_solutions(
            clean_solution_ids=have_to_update_clean_solution_ids_list,
            clean_solution_dtos=have_to_update_clean_solutions_list
        )
        return
