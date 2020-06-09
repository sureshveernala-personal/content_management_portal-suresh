from typing import List
from content_management_portal.dtos.dtos import PrefilledCodeDto
from content_management_portal.interactors.storages.dtos import \
    PrefilledCodeWithQuestionIdDto
from content_management_portal.interactors.storages.\
    prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.models import PrefilledCode


class PrefilledCodeStorageImplementation(PrefilledCodeStorageInterface):

    def is_valid_prefilled_code_id(self, prefilled_code_id: int):
        is_valid = PrefilledCode.objects.filter(id=prefilled_code_id).exists()
        return is_valid


    def is_prefilled_code_belongs_to_question(
            self, question_id: int, prefilled_code_id: int
        ):
        is_valid = PrefilledCode.objects.filter(
            id=prefilled_code_id, question_id=question_id
        ).exists()
        return is_valid


    def get_prefilled_code_ids(self):
        prefilled_code_ids = PrefilledCode.objects.all()\
                                          .values_list('id', flat=True)
        return list(prefilled_code_ids)


    def get_question_prefilled_code_ids(self, question_id: int):
        prefilled_code_ids = PrefilledCode.objects.filter(
            question_id=question_id
        ).values_list('id', flat=True)
        return list(prefilled_code_ids)


    def create_prefilled_codes(
            self,
            question_id: int,
            prefilled_code_dtos: List[PrefilledCodeDto]
        ):
        prefilled_code_objs = [
            PrefilledCode(
                question_id=question_id,
                language=solution.language,
                solution_content=solution.solution_content,
                file_name=solution.file_name
            )
            for solution in prefilled_code_dtos
        ]
        PrefilledCode.objects.bulk_create(prefilled_code_objs)
        return


    def update_prefilled_codes(
            self,
            prefilled_code_ids,
            prefilled_code_dtos: List[PrefilledCodeDto]
        ):
        prefilled_codes = PrefilledCode.objects.filter(
            id__in=prefilled_code_ids
        )
        prefilled_code_dict = {
            prefilled_code_dto.prefilled_code_id: prefilled_code_dto
            for prefilled_code_dto in prefilled_code_dtos
        }
        for prefilled_code in prefilled_codes:
            id = prefilled_code.id
            prefilled_code.language = prefilled_code_dict[id].language
            prefilled_code.solution_content = prefilled_code_dict[id].\
                solution_content
            prefilled_code.file_name = prefilled_code_dict[id].file_name

        prefilled_codes.bulk_update(
            prefilled_codes,
            ['language', 'solution_content', 'file_name']
        )
        return


    def delete_prefilled_code(self, prefilled_code_id: int):
        PrefilledCode.objects.get(id=prefilled_code_id).delete()
        return


    @staticmethod
    def _convert_prefilled_code_into_dto(prefilled_code):
        prefilled_code_dto = PrefilledCodeWithQuestionIdDto(
            language=prefilled_code.language,
            solution_content=prefilled_code.solution_content,
            file_name=prefilled_code.file_name,
            prefilled_code_id=prefilled_code.id,
            question_id=prefilled_code.question_id
        )
        return prefilled_code_dto


    def get_prefilled_codes(
            self, question_id: int
        ) -> PrefilledCodeWithQuestionIdDto:
        prefilled_codes = PrefilledCode.objects.filter(question_id=question_id)
        prefilled_code_with_question_id_dto = [
            self._convert_prefilled_code_into_dto(
                prefilled_code=prefilled_code
            )
            for prefilled_code in prefilled_codes
        ]
        return prefilled_code_with_question_id_dto
