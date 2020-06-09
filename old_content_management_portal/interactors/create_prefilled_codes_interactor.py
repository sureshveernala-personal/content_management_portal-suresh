from content_management_portal.interactors.storages.\
    prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface

from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, List
from content_management_portal.dtos.dtos import PrefilledCodeDto


class CreatePrefilledCodesInteractor:
    def __init__(
            self,
            prefilled_code_storage: PrefilledCodeStorageInterface,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.prefilled_code_storage = prefilled_code_storage
        self.presenter = presenter
        self.problem_statement_storage = problem_statement_storage

    def create_prefilled_codes(
            self, question_id: str, prefilled_codes: List[Dict]
        ):
        is_invalid_question_id = not self.problem_statement_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
            return
        prefilled_code_dtos_list = self._get_prefilled_codes_dtos_list(
            prefilled_codes
        )
        self._update_prefilled_codes(
            prefilled_code_dtos_list=prefilled_code_dtos_list,
            question_id=question_id
        )
        self._create_new_prefilled_codes(
            prefilled_code_dtos_list=prefilled_code_dtos_list,
            question_id=question_id
        )
        new_prefilled_code_dtos = self.prefilled_code_storage.\
            get_prefilled_codes(question_id=question_id)
        question_id_dict = self.presenter.get_create_prefilled_codes_response(
            prefilled_codes_dto_with_question_id=new_prefilled_code_dtos
        )
        return question_id_dict


    @staticmethod
    def _get_prefilled_codes_dtos_list(prefilled_codes: List):
        prefilled_code_dtos_list = [
            PrefilledCodeDto(
                language=solution['language'],
                solution_content=solution['solution_content'],
                file_name=solution['file_name'],
                prefilled_code_id=solution['prefilled_code_id']
            )
            for solution in prefilled_codes
        ]
        return prefilled_code_dtos_list


    def _valiadate_prefilled_code(
            self, total_prefilled_codes: List[int],
            question_prefilled_codes: List[int], prefilled_code_id: int
        ):
        is_invalid_prefilled_code_id = prefilled_code_id not in \
            total_prefilled_codes
        if is_invalid_prefilled_code_id:
            self.presenter.raise_invalid_prefilled_code_id_exception()
            return
        is_not_questions_prefilled_code_id = prefilled_code_id not in\
            question_prefilled_codes
        if is_not_questions_prefilled_code_id:
            self.presenter.\
                raise_prefilled_code_not_belongs_to_question_exception()
        return


    def _create_new_prefilled_codes(
            self,
            prefilled_code_dtos_list: List[PrefilledCodeDto],
            question_id: int
        ):
        have_to_create_prefilled_codes_list = [
            solution_dto
            for solution_dto in prefilled_code_dtos_list
            if solution_dto.prefilled_code_id is None
        ]

        self.prefilled_code_storage.create_prefilled_codes(
            question_id=question_id,
            prefilled_code_dtos=have_to_create_prefilled_codes_list
        )
        return
    
    def _update_prefilled_codes(
            self, prefilled_code_dtos_list: List[PrefilledCodeDto],
            question_id: int
        ):
        have_to_update_prefilled_codes_list =[]
        have_to_update_prefilled_code_ids_list =[]
        for prefilled_code_dto in prefilled_code_dtos_list:
            is_update = prefilled_code_dto.prefilled_code_id is not None
            if is_update:
                have_to_update_prefilled_code_ids_list.append(
                    prefilled_code_dto.prefilled_code_id
                )
                have_to_update_prefilled_codes_list.append(prefilled_code_dto)
        print(have_to_update_prefilled_code_ids_list)
        total_prefilled_codes = \
            self.prefilled_code_storage.get_prefilled_code_ids()
        question_prefilled_codes = \
            self.prefilled_code_storage.get_question_prefilled_code_ids(
                question_id=question_id
            )
        for prefilled_code_id in have_to_update_prefilled_code_ids_list:
            self._valiadate_prefilled_code(
                prefilled_code_id=prefilled_code_id,
                total_prefilled_codes=total_prefilled_codes,
                question_prefilled_codes=question_prefilled_codes
            )
        self.prefilled_code_storage.update_prefilled_codes(
            prefilled_code_ids=have_to_update_prefilled_code_ids_list,
            prefilled_code_dtos=have_to_update_prefilled_codes_list
        )
        return
