from content_management_portal.interactors.storages.dtos import HintDto,\
    HintWithQuestionIdDto, DescriptionDto, HintsSwapDetailsDto
from content_management_portal.interactors.storages.\
    hint_storage_interface import HintStorageInterface
from content_management_portal.models.hint import Hint
from typing import List
from django.db.models import Max


class HintStorageImplementation(HintStorageInterface):

    def is_valid_hint_id(self, hint_id: int) -> bool:
        is_valid_hint_id = Hint.objects.filter(id=hint_id)\
                                                .exists()
        return is_valid_hint_id


    def is_hint_belongs_to_question(
            self, question_id: int, hint_id: int
        ):
        is_hint_belongs_to_question = Hint.objects.filter(
            id=hint_id, question_id=question_id
        ).exists()
        return is_hint_belongs_to_question


    def get_max_hint_number(self, question_id: int):
        max_number_dict = Hint.objects.filter(question_id=question_id)\
                                      .aggregate(Max('hint_number'))
        max_number =  max_number_dict['hint_number__max']
        return max_number


    def create_hint(
            self, question_id, hint_details: HintDto
        ) -> int:
        hint_number = hint_details.hint_number
        content = hint_details.content
        content_type = hint_details.content_type
        title = hint_details.title

        hint = Hint.objects.create(
            question_id=question_id,
            hint_number=hint_number, content=content, title=title,
            content_type=content_type
        )
        hint_dto = self._convert_hint_object_into_dto(
            hint=hint
        )
        return hint_dto


    def update_hint(
            self, hint_details: HintDto
        ) -> int:
        hint_id = hint_details.hint_id
        hint = Hint.objects.get(id=hint_id)
        hint.hint_number = hint_details.hint_number
        hint.content = hint_details.content
        hint.content_type = hint_details.content_type
        hint.title = hint_details.title
        hint.save()
        hint_dto = self._convert_hint_object_into_dto(
            hint=hint
        )
        return hint_dto


    def delete_hint(self, question_id: int, hint_id: int):
        hint = Hint.objects.get(id=hint_id)
        hint_number = hint.hint_number
        hint.delete()
        return hint_number


    def decrease_hint_numbers_followed_given_hint_number(
            self, question_id: int, hint_number: int
        ):
        hints = Hint.objects.filter(
            question_id=question_id, hint_number__gt=hint_number
        )
        for hint in hints:
            hint.hint_number -= 1
        hints.bulk_update(hints, ['hint_number'])
        return


    def swap_hints(
            self, hints_swap_details: HintsSwapDetailsDto
        ):
        hint_ids = [
            hints_swap_details.first_hint_id,
            hints_swap_details.second_hint_id
        ]
        hints = Hint.objects.filter(id__in=hint_ids)
        create_cache = len(hints)
        first_hint_number = hints_swap_details.first_hint_number
        second_hint_number = hints_swap_details.second_hint_number
        hints[0].hint_number = first_hint_number
        hints[1].hint_number = second_hint_number
        hints.bulk_update(hints, ['hint_number'])
        return


    def get_hint_ids(self) -> List[int]:
        hint_ids = Hint.objects.all().values_list('id', flat=True)
        return list(hint_ids)


    def get_given_question_hint_ids(self, question_id: int) -> List[int]:
        hint_ids = Hint.objects.filter(
            question_id=question_id
        ).values_list('id', flat=True)
        return list(hint_ids)


    @staticmethod
    def _convert_hint_object_into_dto(hint: Hint):
        hint_with_question_id_dto = HintWithQuestionIdDto(
            question_id=hint.question_id,
            hint_id=hint.id,
            title=hint.title,
            hint_number=hint.hint_number,
            content=hint.content,
            content_type=hint.content_type
        )
        return hint_with_question_id_dto
