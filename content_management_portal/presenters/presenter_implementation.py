from datetime import datetime
from typing import List, Dict
import json
from django.http import response
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden,\
    BadRequest
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface, CreateProblemStatementPresenterInterface
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionWithQuestionIdDto, QuestionStatusDto,\
    RoughSolutionDto, TestCaseWithQuestionIdDto,\
    TestCaseDto, QuestionDto, PrefilledCodeWithQuestionIdDto,\
    PrefilledCodeDto, CleanSolutionWithQuestionIdDto, CleanSolutionDto,\
    HintWithQuestionIdDto, DescriptionDto, HintDto, SolutionApproachDto,\
    UserDto
from content_management_portal.constants.exception_messages import\
    INVALID_QUESTION_ID, INVALID_ROUGH_SOLUTION_ID,\
    ROUGH_SOLUTION_NOT_BELONG_TO_QUESTION, INVALID_USER_NAME, INVALID_PASSWORD,\
    INVALID_OFFSET_VALUE, INVALID_LIMIT_VALUE, INVALID_TEST_CASE_ID,\
    TEST_CASE_NOT_BELONG_TO_QUESTION, INVALID_PREFILLED_CODE_ID,\
    PREFILLED_CODE_NOT_BELONG_TO_QUESTION, INVALID_CLEAN_SOLUTION_ID,\
    CLEAN_SOLUTION_NOT_BELONG_TO_QUESTION, INVALID_HINT_ID,\
    HINT_NOT_BELONG_TO_QUESTION, INVALID_FIRST_TEST_CASE_ID,\
    INVALID_SECOND_TEST_CASE_ID, INVALID_FIRST_HINT_ID,\
    INVALID_SECOND_HINT_ID, SOLUTION_APPROACH_NOT_BELONG_TO_QUESTION,\
    INVALID_SOLUTION_APPROACH_ID,\
    CAN_NOT_CREATE_MORE_THEN_ONE_SOLUTION_APPROACH
from content_management_portal.presenters.mixins import QuestionValidationMixin


class CreateProblemStatementPresenterImplementation(
        QuestionValidationMixin, CreateProblemStatementPresenterInterface
    ):

    def get_create_problem_statement_response(
            self, question_dto: QuestionDto
        ) -> response.HttpResponse:
        question_dict = {
            "question_id": question_dto.question_id,
            "short_text": question_dto.short_text,
            "problem_description": {
                "content": question_dto.content,
                "content_type": question_dto.content_type
            }
        }

        data = json.dumps(question_dict)
        return response.HttpResponse(data, status=201)


class PresenterImplementation(QuestionValidationMixin, PresenterInterface):

    def raise_invalid_rough_solution_exception(self):
        raise NotFound(*INVALID_ROUGH_SOLUTION_ID)


    def raise_rough_solution_not_belongs_to_question_exception(self):
        raise BadRequest(*ROUGH_SOLUTION_NOT_BELONG_TO_QUESTION)


    def get_create_rough_solutions_response(
            self, question_id: int,
            rough_solution_with_question_id_dtos: \
                RoughSolutionWithQuestionIdDto
        ):
        rough_solution_dicts = self._get_rough_solution_dicts_list(
            rough_solution_dtos=rough_solution_with_question_id_dtos
        )

        rough_solution_with_question_id_dict = {
            "question_id": question_id,
            "rough_solutions": rough_solution_dicts
        }
        return rough_solution_with_question_id_dict

    def _get_rough_solution_dicts_list(
            self, rough_solution_dtos: List[RoughSolutionWithQuestionIdDto]
        ) -> List:
        rough_solution_dicts = [
            self._get_rough_solution_dict(
                rough_solution=rough_solution_dto
            )
            for rough_solution_dto in rough_solution_dtos
        ]
        return rough_solution_dicts

    @staticmethod
    def _get_rough_solution_dict(
            rough_solution: RoughSolutionWithQuestionIdDto
        ) -> Dict:
        rough_solution_dict = {
            "language": rough_solution.language,
            "solution_content": rough_solution.solution_content,
            "file_name": rough_solution.file_name,
            "rough_solution_id": rough_solution.rough_solution_id
        }
        return rough_solution_dict


    def get_create_test_case_response(
            self, question_id: int,
            test_case_with_question_id_dto: TestCaseWithQuestionIdDto
        ):
        test_case_complete_details_dict = {
            "question_id": question_id,
            "test_case": self._get_test_case_dict(
                test_case=test_case_with_question_id_dto
            )
        }
        return test_case_complete_details_dict


    def raise_invalid_test_case_id_exception(self):
        raise NotFound(*INVALID_TEST_CASE_ID)


    def raise_test_case_not_belongs_to_question_exception(self):
        raise BadRequest(*TEST_CASE_NOT_BELONG_TO_QUESTION)


    def raise_invalid_hint_id_exception(self):
        raise NotFound(*INVALID_HINT_ID)


    def raise_hint_not_belongs_to_question_exception(self):
        raise BadRequest(*HINT_NOT_BELONG_TO_QUESTION)


    def get_create_hint_response(
            self, question_id: int,
            hint_with_question_id_dto: HintWithQuestionIdDto
        ):
        hint_with_question_id_dict = {
            "question_id": question_id,
            "hint": self._get_hint_dict(hint=hint_with_question_id_dto)
        }
        return hint_with_question_id_dict


    def raise_invalid_prefilled_code_id_exception(self):
        raise NotFound(*INVALID_PREFILLED_CODE_ID)


    def raise_prefilled_code_not_belongs_to_question_exception(self):
        raise BadRequest(*PREFILLED_CODE_NOT_BELONG_TO_QUESTION)


    def get_create_prefilled_codes_response(
            self,
            question_id: int,
            prefilled_code_with_question_id_dtos: \
            PrefilledCodeWithQuestionIdDto
        ):
        prefilled_code_dicts = self._get_prefilled_code_dicts_list(
            prefilled_code_dtos=prefilled_code_with_question_id_dtos
        )
        prefilled_code_with_question_id_dict = {
            "question_id": question_id,
            "prefilled_codes": prefilled_code_dicts
        }
        return prefilled_code_with_question_id_dict
    
    @staticmethod
    def _get_prefilled_code_dict(
            prefilled_code: PrefilledCodeWithQuestionIdDto
        ) -> Dict:
        prefilled_code_dict = {
            "language": prefilled_code.language,
            "solution_content": prefilled_code.solution_content,
            "file_name": prefilled_code.file_name,
            "prefilled_code_id": prefilled_code.prefilled_code_id
        }
        return prefilled_code_dict


    def _get_prefilled_code_dicts_list(
            self, prefilled_code_dtos: List[PrefilledCodeWithQuestionIdDto]
        ):
        prefilled_code_dicts = [
            self._get_prefilled_code_dict(prefilled_code=prefilled_code_dto)
            for prefilled_code_dto in prefilled_code_dtos
        ]
        return prefilled_code_dicts


    def raise_invalid_clean_solution_id_exception(self):
        raise NotFound(*INVALID_CLEAN_SOLUTION_ID)


    def raise_clean_solution_not_belongs_to_question_exception(self):
        raise BadRequest(*CLEAN_SOLUTION_NOT_BELONG_TO_QUESTION)


    def get_create_clean_solutions_response(
            self,
            question_id: int,
            clean_solution_with_question_id_dtos: \
            CleanSolutionWithQuestionIdDto
        ):
        clean_solution_dicts = [
            self._get_clean_solution_dict(
                clean_solution=clean_solution_dto
            )
            for clean_solution_dto in clean_solution_with_question_id_dtos
        ]
        clean_solution_with_question_id_dict = {
            "question_id": question_id,
            "clean_solutions": clean_solution_dicts
        }
        return clean_solution_with_question_id_dict


    def get_questions_response(
            self, question_status_dtos: List[QuestionStatusDto],
            total_questions: int, offset: int, limit: int):
        questions_list = [
            self._get_question_status_dict(question_status_dto)
            for question_status_dto in question_status_dtos
        ]
        questions_dict = {
            "total_questions": total_questions,
            "offset": offset,
            "limit": limit,
            "questions_list": questions_list
        }
        return questions_dict


    @staticmethod
    def _get_question_status_dict(question_status_dto: QuestionStatusDto):
        question_status_dict = {
            "question_id": question_status_dto.question_id,
            "statement": question_status_dto.statement,
            "rough_solution_status": question_status_dto.rough_solution_status,
            "test_cases_status": question_status_dto.test_cases_status,
            "prefilled_code_status": question_status_dto.prefilled_code_status,
            "solution_approach_status": \
                question_status_dto.solution_approach_status,
            "clean_solution_status": question_status_dto.clean_solution_status
        }
        return question_status_dict


    def raise_invalid_offset_value_exception(self):
        raise BadRequest(*INVALID_OFFSET_VALUE)


    def raise_invalid_limit_value_exception(self):
        raise BadRequest(*INVALID_LIMIT_VALUE)


    def get_question_details_response(
            self,
            question_dto: QuestionDto,
            rough_solution_dtos: List[RoughSolutionDto],
            clean_solution_dtos: List[CleanSolutionDto],
            test_case_dtos: List[TestCaseDto],
            solution_approach_dto: SolutionApproachDto,
            hint_dtos: List[HintDto],
            prefilled_code_dtos: List[PrefilledCodeDto]
        ):
        statement_dict = self._get_statement_dict(question_dto)
        rough_solution_dicts = self._get_rough_solution_dicts_list(
            rough_solution_dtos=rough_solution_dtos
        )
        clean_solution_dicts = self._get_clean_solution_dicts_list(
            clean_solution_dtos=clean_solution_dtos
        )
        test_case_dicts = self._get_test_case_dicts_list(
            test_case_dtos=test_case_dtos
        )
        if solution_approach_dto:
            solution_approach_dict = self._get_solution_approach_dict(
                solution_approach=solution_approach_dto
            )
        else:
            solution_approach_dict = None

        hint_dicts=self._get_hint_dicts_list(hint_dtos=hint_dtos)
        prefilled_code_dicts = self._get_prefilled_code_dicts_list(
            prefilled_code_dtos=prefilled_code_dtos
        )
        question_details_dict = {
            "question_id": question_dto.question_id,
            "statement": statement_dict,
            "rough_solutions": rough_solution_dicts,
            "clean_solutions": clean_solution_dicts,
            "test_cases": test_case_dicts,
            "solution_approach": solution_approach_dict,
            "hints": hint_dicts,
            "prefilled_codes": prefilled_code_dicts
        }
        return question_details_dict

    def _get_statement_dict(self, question: QuestionDto) -> Dict:
        statement_dict = {
            "short_text": question.short_text,
            "problem_description": {
                "content": question.content,
                "content_type": question.content_type
            }
        }
        return statement_dict
    
    # @staticmethod
    # def _get_prefilled_code_dict(
    #         prefilled_code: PrefilledCodeWithQuestionIdDto
    #     ) -> Dict:
    #     prefilled_code_dict = {
    #         "language": prefilled_code.language,
    #         "solution_content": prefilled_code.solution_content,
    #         "file_name": prefilled_code.file_name,
    #         "prefilled_code_id": prefilled_code.prefilled_code_id
    #     }
    #     return prefilled_code_dict


    # def _get_prefilled_code_dicts_list(
    #         self, prefilled_code_dtos: List[PrefilledCodeWithQuestionIdDto]
    #     ):
    #     prefilled_code_dicts = [
    #         self._get_prefilled_code_dict(prefilled_code=prefilled_code_dto)
    #         for prefilled_code_dto in prefilled_code_dtos
    #     ]
    #     return prefilled_code_dicts


    def get_create_solution_approach_response(
            self, question_id: int, solution_approach_dto: SolutionApproachDto
        ):
        solution_approach_dict = {
            "question_id": question_id,
            "solution_approach": self._get_solution_approach_dict(
                solution_approach=solution_approach_dto
            )
        }
        return solution_approach_dict


    def raise_invalid_solution_approach_id_exception(self):
        raise NotFound(*INVALID_SOLUTION_APPROACH_ID)


    def raise_solution_approach_not_belongs_to_question_exception(self):
        raise BadRequest(*SOLUTION_APPROACH_NOT_BELONG_TO_QUESTION)


    def raise_can_not_create_more_then_one_question(self):
        raise BadRequest(*CAN_NOT_CREATE_MORE_THEN_ONE_SOLUTION_APPROACH)


    def get_question_user_response(self, user_dto: UserDto):
        user_dict = self._get_user_dict(user_dto=user_dto)
        return user_dict


    @staticmethod
    def _get_user_dict(user_dto: UserDto):
        user_dict = {
            "username": user_dto.username,
            "user_id": user_dto.user_id
        }
        return user_dict



    @staticmethod
    def _get_clean_solution_dict(
            clean_solution: CleanSolutionWithQuestionIdDto
        ) -> Dict:
        clean_solution_dict = {
            "language": clean_solution.language,
            "solution_content": clean_solution.solution_content,
            "file_name": clean_solution.file_name,
            "clean_solution_id": clean_solution.clean_solution_id
        }
        return clean_solution_dict


    def _get_clean_solution_dicts_list(
            self, clean_solution_dtos: List[CleanSolutionWithQuestionIdDto]
        ):
        clean_solution_dicts = [
            self._get_clean_solution_dict(clean_solution=clean_solution_dto)
            for clean_solution_dto in clean_solution_dtos
        ]
        return clean_solution_dicts


    @staticmethod
    def _get_test_case_dict(test_case: TestCaseWithQuestionIdDto) -> Dict:
        test_case_dict ={
            "test_case_number": test_case.test_case_number,
            "input": test_case.input,
            "output": test_case.output,
            "score": test_case.score,
            "is_hidden": test_case.is_hidden,
            "test_case_id": test_case.test_case_id
        }
        return test_case_dict


    def _get_test_case_dicts_list(
            self, test_case_dtos: List[TestCaseWithQuestionIdDto]
        ):
        test_case_dicts_list = [
            self._get_test_case_dict(test_case=test_case_dto)
            for test_case_dto in test_case_dtos
        ]
        return test_case_dicts_list


    def _get_hint_dict(self, hint: HintWithQuestionIdDto) -> Dict:
        hint_dict = {
            "hint_id": hint.hint_id,
            "hint_number": hint.hint_number,
            "title": hint.title,
            "description": {
                "content": hint.content,
                "content_type": hint.content_type
            }
        }
        return hint_dict


    def _get_hint_dicts_list(
            self, hint_dtos: List[HintWithQuestionIdDto]
        ):
        hint_dicts_list = [
            self._get_hint_dict(hint=hint_dto)
            for hint_dto in hint_dtos
        ]
        return hint_dicts_list


    @staticmethod
    def _get_description_dict(description: DescriptionDto) -> Dict:
        description_dict = {
            "content": description.content,
            "content_type": description.content_type
        }
        return description_dict


    @staticmethod
    def _get_solution_approach_dict(solution_approach: SolutionApproachDto):
        solution_approach_dict = {
            "title": solution_approach.title,
            "description": {
                "content": solution_approach.description_content,
                "content_type": \
                solution_approach.description_content_type,
            },
            "complexity_analysis": {
                "content": solution_approach.complexity_analysis_content,
                "content_type": \
                solution_approach.complexity_analysis_content_type
            },
            "solution_approach_id": solution_approach.solution_approach_id
        }
        return solution_approach_dict
