from typing import List
from content_management_portal.dtos.dtos import RoughSolutionDto
from content_management_portal.interactors.storages.dtos import \
    RoughSolutionsWithQuestionIdDto
from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.models import RoughSolution


class RoughSolutionStorageImplementation(RoughSolutionStorageInterface):

    def is_valid_rough_solution_id(self, rough_solution_id: int):
        is_valid = RoughSolution.objects.filter(id=rough_solution_id).exists()
        return is_valid

    def is_rough_solution_belongs_to_question(
            self, question_id: int, rough_solution_id: int
        ):
        is_valid = RoughSolution.objects.filter(
            id=rough_solution_id, question_id=question_id
        ).exists()
        return is_valid

    def get_rough_solution_ids(self):
        rough_solution_ids = RoughSolution.objects.all()\
                                          .values_list('id', flat=True)
        return list(rough_solution_ids)

    def get_question_rough_solution_ids(self, question_id: int):
        rough_solution_ids = RoughSolution.objects.filter(
            question_id=question_id
        ).values_list('id', flat=True)
        return list(rough_solution_ids)

    def create_rough_solutions(
            self,
            question_id: int,
            rough_solutions_dtos: List[RoughSolutionDto]
        ):
        rough_solution_objs = [
            RoughSolution(
                question_id=question_id,
                language=solution.language,
                solution_content=solution.solution_content,
                file_name=solution.file_name
            )
            for solution in rough_solutions_dtos
        ]
        RoughSolution.objects.bulk_create(rough_solution_objs)
        return

    def update_rough_solutions(
            self,
            rough_solution_ids,
            rough_solution_dtos: List[RoughSolutionDto]
        ):
        rough_solutions = RoughSolution.objects.filter(
            id__in=rough_solution_ids
        )
        rough_solution_dict = {
            rough_solution_dto.rough_solution_id: rough_solution_dto
            for rough_solution_dto in rough_solution_dtos
        }
        for rough_solution in rough_solutions:
            id = rough_solution.id
            rough_solution.language = rough_solution_dict[id].language
            rough_solution.solution_content = rough_solution_dict[id].\
                solution_content
            rough_solution.file_name = rough_solution_dict[id].file_name
        rough_solutions.bulk_update(
            rough_solutions,
            ['language', 'solution_content', 'file_name']
        )
        return

    def delete_rough_solution(self, rough_solution_id: int):
        RoughSolution.objects.get(id=rough_solution_id).delete()
        return

    @staticmethod
    def _convert_rough_solution_into_dto(rough_solution):
        rough_solution_dto = RoughSolutionDto(
            language=rough_solution.language,
            solution_content=rough_solution.solution_content,
            file_name=rough_solution.file_name,
            rough_solution_id=rough_solution.id
        )
        return rough_solution_dto

    def get_rough_solutions(
            self, question_id: int
        ) -> RoughSolutionsWithQuestionIdDto:
        rough_solutions = RoughSolution.objects.filter(question_id=question_id)
        rough_solution_dtos = [
            self._convert_rough_solution_into_dto(
                rough_solution=rough_solution
            )
            for rough_solution in rough_solutions
        ]
        rough_solution_with_question_id_dto = RoughSolutionsWithQuestionIdDto(
            question_id=question_id,
            rough_solutions=rough_solution_dtos
        )
        return rough_solution_with_question_id_dto

