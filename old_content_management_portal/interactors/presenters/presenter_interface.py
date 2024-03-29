from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionsWithQuestionIdDto, QuestionsDto,\
    TestCaseWithQuestionIdDto, QuestionDto, PrefilledCodesWithQuestionIdDto,\
    CleanSolutionsWithQuestionIdDto, HintWithQuestionIdDto, HintDto,\
    SolutionApproachDto, RoughSolutionDto, CleanSolutionDto, TestCaseDto,\
    PrefilledCodeDto


class PresenterInterface(ABC):
    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def login_response(self, access_token):
        pass

    @abstractmethod
    def raise_invalid_question_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_rough_solution_exception(self):
        pass

    @abstractmethod
    def raise_rough_solution_not_belongs_to_question_exception(self):
        pass

    @abstractmethod
    def get_create_problem_statement_response(self, question_dto: QuestionDto):
        pass

    @abstractmethod
    def get_create_rough_solutions_response(
            self,
            rough_solutions_dto_with_question_id: \
            RoughSolutionsWithQuestionIdDto
        ):
        pass

    @abstractmethod
    def raise_invalid_prefilled_code_id_exception(self):
        pass

    @abstractmethod
    def raise_prefilled_code_not_belongs_to_question_exception(self):
        pass

    @abstractmethod
    def get_create_prefilled_codes_response(
            self,
            prefilled_codes_dto_with_question_id: \
            PrefilledCodesWithQuestionIdDto
        ):
        pass

    @abstractmethod
    def raise_invalid_test_case_id_exception(self):
        pass

    @abstractmethod
    def raise_test_case_not_belongs_to_question_exception(self):
        pass

    @abstractmethod
    def get_create_test_case_response(
            self, test_case_with_question_id_dto: TestCaseWithQuestionIdDto
        ):
        pass

    @abstractmethod
    def raise_invalid_hint_id_exception(self):
        pass

    @abstractmethod
    def raise_hint_not_belongs_to_question_exception(self):
        pass

    @abstractmethod
    def get_create_hint_response(
            self, hint_with_question_id_dto: HintWithQuestionIdDto
        ):
        pass

    @abstractmethod
    def raise_invalid_clean_solution_id_exception(self):
        pass

    @abstractmethod
    def raise_clean_solution_not_belongs_to_question_exception(self):
        pass

    @abstractmethod
    def get_create_clean_solutions_response(
            self,
            clean_solutions_dto_with_question_id: \
            CleanSolutionsWithQuestionIdDto
        ):
        pass

    @abstractmethod
    def get_create_solution_approach_response(
            self, question_id: int, solution_approach_dto: SolutionApproachDto
        ):
        pass

    @abstractmethod
    def raise_invalid_solution_approach_id_exception(self):
        pass
    
    @abstractmethod
    def raise_solution_approach_not_belongs_to_question_exception(self):
        pass


    @abstractmethod
    def get_questions_response(self, questions_dto: QuestionsDto):
        pass

    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
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
        pass