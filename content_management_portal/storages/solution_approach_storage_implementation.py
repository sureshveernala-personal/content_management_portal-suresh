from content_management_portal.interactors.storages.dtos import \
    SolutionApproachDto
from content_management_portal.interactors.storages.\
    solution_approach_storage_interface import SolutionApproachStorageInterface
from content_management_portal.models.solution_approach import SolutionApproach
from typing import List


class SolutionApproachStorageImplementation(SolutionApproachStorageInterface):

    def is_valid_solution_approach_id(self, solution_approach_id: int) -> bool:
        is_valid_solution_approach_id = \
            SolutionApproach.objects.filter(id=solution_approach_id).exists()
        return is_valid_solution_approach_id

    def is_solution_approach_belongs_to_question(
            self, question_id: int, solution_approach_id: int
        ):
        is_solution_approach_belongs_to_question =\
            SolutionApproach.objects.filter(
                id=solution_approach_id, question_id=question_id
            ).exists()
        return is_solution_approach_belongs_to_question

    def create_solution_approach(
            self, question_id, solution_approach_details: SolutionApproachDto
        ) -> int:
        description_content = solution_approach_details.description_content
        description_content_type = \
            solution_approach_details.description_content_type
        complexity_analysis_content = \
            solution_approach_details.complexity_analysis_content
        complexity_analysis_content_type = \
            solution_approach_details.complexity_analysis_content_type
        title = solution_approach_details.title

        solution_approach = SolutionApproach.objects.create(
            question_id=question_id, title=title,
            description_content=description_content,
            description_content_type=description_content_type,
            complexity_analysis_content=complexity_analysis_content,
            complexity_analysis_content_type=complexity_analysis_content_type
        )
        solution_approach_dto = self._convert_solution_approach_object_into_dto(
            solution_approach=solution_approach
        )
        return solution_approach_dto

    def update_solution_approach(
            self, solution_approach_details: SolutionApproachDto
        ) -> int:
        solution_approach_id = solution_approach_details.solution_approach_id
        solution_approach = SolutionApproach.objects.get(
            id=solution_approach_id
        )
        solution_approach.title = solution_approach_details.title
        solution_approach.description_content = \
            solution_approach_details.description_content
        solution_approach.description_content_type = \
            solution_approach_details.description_content_type
        solution_approach.complexity_analysis_content = \
            solution_approach_details.complexity_analysis_content
        solution_approach.complexity_analysis_content_type = \
            solution_approach_details.complexity_analysis_content_type
        solution_approach.save()
        solution_approach_dto = self._convert_solution_approach_object_into_dto(
            solution_approach=solution_approach
        )
        return solution_approach_dto


    @staticmethod
    def _convert_solution_approach_object_into_dto(
            solution_approach: SolutionApproach
        ):
        solution_approach_dto = SolutionApproachDto(
            solution_approach_id=solution_approach.id,
            title=solution_approach.title,
            description_content=solution_approach.description_content,
            description_content_type=solution_approach.description_content_type,
            complexity_analysis_content=\
                solution_approach.complexity_analysis_content,
            complexity_analysis_content_type=\
                solution_approach.complexity_analysis_content_type,
        )
        return solution_approach_dto
