from typing import List
from content_management_portal.dtos.dtos import CleanSolutionDto
from content_management_portal.interactors.storages.dtos import \
    CleanSolutionsWithQuestionIdDto
from content_management_portal.interactors.storages.\
    clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.models import CleanSolution


class CleanSolutionStorageImplementation(CleanSolutionStorageInterface):

    def is_valid_clean_solution_id(self, clean_solution_id: int):
        is_valid = CleanSolution.objects.filter(id=clean_solution_id).exists()
        return is_valid

    def is_clean_solution_belongs_to_question(
            self, question_id: int, clean_solution_id: int
        ):
        is_valid = CleanSolution.objects.filter(
            id=clean_solution_id, question_id=question_id
        ).exists()
        return is_valid

    def get_clean_solution_ids(self):
        clean_solution_ids = CleanSolution.objects.all()\
                                          .values_list('id', flat=True)
        return list(clean_solution_ids)

    def get_question_clean_solution_ids(self, question_id: int):
        clean_solution_ids = CleanSolution.objects.filter(
            question_id=question_id
        ).values_list('id', flat=True)
        return list(clean_solution_ids)

    def create_clean_solutions(
            self,
            question_id: int,
            clean_solution_dtos: List[CleanSolutionDto]
        ):
        clean_solution_objs = [
            CleanSolution(
                question_id=question_id,
                language=solution.language,
                solution_content=solution.solution_content,
                file_name=solution.file_name
            )
            for solution in clean_solution_dtos
        ]
        CleanSolution.objects.bulk_create(clean_solution_objs)
        return

    def update_clean_solutions(
            self,
            clean_solution_ids,
            clean_solution_dtos: List[CleanSolutionDto]
        ):
        clean_solutions = CleanSolution.objects.filter(
            id__in=clean_solution_ids
        )
        clean_solution_dict = {
            clean_solution_dto.clean_solution_id: clean_solution_dto
            for clean_solution_dto in clean_solution_dtos
        }
        for clean_solution in clean_solutions:
            id = clean_solution.id
            clean_solution.language = clean_solution_dict[id].language
            clean_solution.solution_content = clean_solution_dict[id].\
                solution_content
            clean_solution.file_name = clean_solution_dict[id].file_name
        clean_solutions.bulk_update(
            clean_solutions,
            ['language', 'solution_content', 'file_name']
        )
        return

    def delete_clean_solution(self, clean_solution_id: int):
        CleanSolution.objects.get(id=clean_solution_id).delete()
        return

    @staticmethod
    def _convert_clean_solution_into_dto(clean_solution):
        clean_solution_dto = CleanSolutionDto(
            language=clean_solution.language,
            solution_content=clean_solution.solution_content,
            file_name=clean_solution.file_name,
            clean_solution_id=clean_solution.id
        )
        return clean_solution_dto

    def get_clean_solutions(
            self, question_id: int
        ) -> CleanSolutionsWithQuestionIdDto:
        clean_solutions = CleanSolution.objects.filter(question_id=question_id)
        clean_solution_dtos = [
            self._convert_clean_solution_into_dto(
                clean_solution=clean_solution
            )
            for clean_solution in clean_solutions
        ]
        clean_solution_with_question_id_dto = CleanSolutionsWithQuestionIdDto(
            question_id=question_id,
            clean_solutions=clean_solution_dtos
        )
        return clean_solution_with_question_id_dto
