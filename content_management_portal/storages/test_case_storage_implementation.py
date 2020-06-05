from content_management_portal.interactors.storages.dtos import TestCaseDto,\
    TestCaseWithQuestionIdDto, TestCasesSwapDetailsDto
from content_management_portal.interactors.storages.\
    test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.models.test_case import TestCase
from typing import List
from django.db.models import Max


class TestCaseStorageImplementation(TestCaseStorageInterface):

    def is_valid_test_case_id(self, test_case_id: int) -> bool:
        is_valid_test_case_id = TestCase.objects.filter(id=test_case_id)\
                                                .exists()
        return is_valid_test_case_id

    def is_test_case_belongs_to_question(
            self, question_id: int, test_case_id: int
        ):
        is_test_case_belongs_to_question = TestCase.objects.filter(
            id=test_case_id, question_id=question_id
        ).exists()
        return is_test_case_belongs_to_question

    def create_test_case(
            self, question_id, test_case_details: TestCaseDto
        ) -> int:
        max_number_dict = TestCase.objects.\
            filter(question_id=question_id).aggregate(Max('test_case_number'))
        max_number = max_number_dict['test_case_number__max']
        if max_number:
            test_case_number = max_number+1#test_case_details.test_case_number
        else:
            test_case_number = 1
        input = test_case_details.input
        output = test_case_details.output
        score = test_case_details.score
        is_hidden = test_case_details.is_hidden

        test_case = TestCase.objects.create(
            question_id=question_id,
            test_case_number=test_case_number, input=input, output=output,
            score=score, is_hidden=is_hidden
        )
        test_case_dto = self._convert_test_case_object_into_dto(
            test_case=test_case
        )
        return test_case_dto

    def update_test_case(
            self, test_case_details: TestCaseDto
        ) -> int:
        test_case_id = test_case_details.test_case_id
        test_case = TestCase.objects.get(id=test_case_id)
        test_case.test_case_number = test_case_details.test_case_number
        test_case.input = test_case_details.input
        test_case.output = test_case_details.output
        test_case.score = test_case_details.score
        test_case.is_hidden = test_case_details.is_hidden
        test_case.save()
        test_case_dto = self._convert_test_case_object_into_dto(
            test_case=test_case
        )
        return test_case_dto

    def delete_test_case(self, question_id: int, test_case_id: int):
        test_case = TestCase.objects.get(id=test_case_id)
        test_case_number = test_case.test_case_number
        test_case.delete()
        test_cases = TestCase.objects.filter(
            question_id=question_id, test_case_number__gt=test_case_number
        )
        for test_case in test_cases:
            test_case.test_case_number -= 1
        test_cases.bulk_update(test_cases, ['test_case_number'])
        return


    def swap_test_cases(
            self, test_cases_swap_details: TestCasesSwapDetailsDto
        ):
        first_test_case_dto = test_cases_swap_details.first_test_case
        second_test_case_dto = test_cases_swap_details.second_test_case
        test_case_ids = [
            first_test_case_dto.test_case_id,
            second_test_case_dto.test_case_id
        ]
        test_cases = TestCase.objects.filter(id__in=test_case_ids)
        create_cache = len(test_cases)
        test_cases[0].test_case_number = first_test_case_dto.test_case_number
        test_cases[1].test_case_number = second_test_case_dto.test_case_number
        test_cases.bulk_update(test_cases, ['test_case_number'])
        return
    
    
    def get_test_case_ids(self) -> List[int]:
        test_case_ids = TestCase.objects.all().values_list('id', flat=True)
        return list(test_case_ids)


    def get_given_question_test_case_ids(self, question_id: int) -> List[int]:
        test_case_ids = TestCase.objects.filter(
            question_id=question_id
        ).values_list('id', flat=True)
        return  list(test_case_ids)


    @staticmethod
    def _convert_test_case_object_into_dto(test_case: TestCase):
        test_case_dto = TestCaseDto(
            test_case_id=test_case.id,
            input=test_case.input,
            output=test_case.output,
            score=test_case.score,
            is_hidden=test_case.is_hidden,
            test_case_number=test_case.test_case_number
        )
        test_case_with_question_id_dto = TestCaseWithQuestionIdDto(
            question_id=test_case.question_id,
            test_case=test_case_dto
        )
        return test_case_with_question_id_dto
