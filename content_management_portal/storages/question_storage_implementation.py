from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.models import Question, RoughSolution,\
    TestCase, CleanSolution, PrefilledCode, SolutionApproach, Hint
from content_management_portal.interactors.storages.dtos import QuestionsDto,\
    QuestionStatusDto, RoughSolutionDto,\
    DescriptionDto, StatementDto, QuestionDto, TestCaseDto, CleanSolutionDto,\
    PrefilledCodeDto, HintDto, SolutionApproachDto


class QuestionStorageImplementation(ProblemStatementStorageInterface):

    def is_valid_question_id(self, question_id):
        is_valid_question = Question.objects.filter(id=question_id).exists()
        return is_valid_question

    def create_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: DescriptionDto
        ) -> int:
        content = description.content
        content_type = description.content_type
        question = Question.objects.create(
            created_by_id=user_id, short_text=short_text, content=content,
            content_type=content_type
        )
        return self._get_question_dto(question)

    def update_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: DescriptionDto,
            question_id: int
        ) -> int:
        content = description.content
        content_type = description.content_type
        question = Question.objects.get(id=question_id)
        question.created_by_id = user_id
        question.short_text = short_text
        question.content = content
        question.content_type = content_type
        question.save()
        return self._get_question_dto(question)

    def delete_problem_statement(
            self,
            question_id: int
        ):
        pass

    def get_questions(self, offset: int, limit: int) -> QuestionsDto:
        total_questions = Question.objects.all().count()
        from_value = offset-1
        to_value = from_value + limit
        if from_value >= total_questions:
            from_value = 0
            to_value = 0
        questions = Question.objects.all().prefetch_related(
            "rough_solutions", "test_cases", "prefilled_codes",
            "clean_solutions", "hints"
        )
        required_questions = questions[from_value:to_value]
        question_status_dtos = [
            self._get_question_status_dto(question)
            for question in required_questions
        ]
        questions_dto = QuestionsDto(
            total_questions=total_questions,
            offset=offset,
            limit=limit,
            questions_list=question_status_dtos
        )
        return questions_dto

    def get_question_details(self, question_id: int):
        question = Question.objects.get(id=question_id)
        question_dto = self._get_question_dto(question)
        rough_solution_dtos = self._get_rough_solution_dtos_list(
            question=question
        )
        clean_solution_dtos = self._get_clean_solution_dtos_list(
            question=question
        )
        test_case_dtos = self._get_test_case_dtos_list(question=question)
        hint_dtos = self._get_hint_dtos_list(question=question)
        try:
            solution_approach = question.solution_approach
            solution_approach_dto = self._get_solution_approach_dto(
            solution_approach=solution_approach
        )
        except Question.solution_approach.RelatedObjectDoesNotExist:
            solution_approach_dto = None
        
        prefilled_code_dtos = self._get_prefilled_code_dtos_list(
            question=question
        )
        return question_dto, rough_solution_dtos, clean_solution_dtos,\
            test_case_dtos, solution_approach_dto, hint_dtos,\
            prefilled_code_dtos

    def _get_question_status_dto(self, question: Question):
        question_status_dto = QuestionStatusDto(
            question_id=question.id,
            statement=question.short_text,
            rough_solution_status=self._does_question_has_rough_solutions(
                question=question
            ),
            test_cases_status=self._does_question_has_test_cases(
                question=question
            ),
            prefilled_code_status=self._does_question_has_prefilled_codes(
                question=question
            ),
            solution_approach_status=self._does_question_has_solution_approach(
                question=question
            ),
            clean_solution_status=self._does_question_has_clean_solutions(
                question=question
            ),
            hint_status=self._does_question_has_hints(question)
        )
        return question_status_dto

    @staticmethod
    def _does_question_has_rough_solutions(question: Question):
        does_question_has_rough_solution = bool(question.rough_solutions.all())
        return does_question_has_rough_solution

    @staticmethod
    def _does_question_has_test_cases(question: Question):
        does_question_has_test_case = bool(question.test_cases.all())
        return does_question_has_test_case

    @staticmethod
    def _does_question_has_prefilled_codes(question: Question):
        does_question_has_prefilled_code = bool(question.prefilled_codes.all())
        return does_question_has_prefilled_code

    @staticmethod
    def _does_question_has_clean_solutions(question: Question):
        does_question_has_clean_solution = bool(question.clean_solutions.all())
        return does_question_has_clean_solution
    
    @staticmethod
    def _does_question_has_hints(question: Question):
        does_question_has_hint = bool(question.hints.all())
        return does_question_has_hint
    
    @staticmethod
    def _does_question_has_solution_approach(question: Question):
        try:
            question.solution_approach
        except Question.solution_approach.RelatedObjectDoesNotExist:
            return False
        return True

    @staticmethod
    def _get_question_dto(question: Question) -> QuestionDto:
        description_dto = DescriptionDto(
            content=question.content,
            content_type=question.content_type
        )
        question_dto = QuestionDto(
            question_id=question.id,
            short_text=question.short_text,
            problem_description=description_dto
        )
        return question_dto


    @staticmethod
    def _get_rough_solution_dto(
            rough_solution: RoughSolution
        ) -> RoughSolutionDto:
        rough_solution_dto = RoughSolutionDto(
            language=rough_solution.language,
            solution_content=rough_solution.solution_content,
            file_name=rough_solution.file_name,
            rough_solution_id=rough_solution.id
        )
        return rough_solution_dto


    def _get_rough_solution_dtos_list(self, question: Question):
        rough_solutions = question.rough_solutions.all()
        rough_solution_dtos = [
            self._get_rough_solution_dto(rough_solution)
            for rough_solution in rough_solutions
        ]
        return rough_solution_dtos


    @staticmethod
    def _get_test_case_dto(test_case: TestCase):
        test_case_dto = TestCaseDto(
            test_case_id=test_case.id,
            input=test_case.input,
            output=test_case.output,
            score=test_case.score,
            is_hidden=test_case.is_hidden,
            test_case_number=test_case.test_case_number
        )
        return test_case_dto

    def _get_test_case_dtos_list(self, question: Question):
        test_cases = question.test_cases.all().order_by('test_case_number')
        test_case_dtos = [
            self._get_test_case_dto(test_case)
            for test_case in test_cases
        ]
        return test_case_dtos

    @staticmethod
    def _get_prefilled_code_dto(prefilled_code: PrefilledCode):
        prefilled_code_dto = PrefilledCodeDto(
            language=prefilled_code.language,
            solution_content=prefilled_code.solution_content,
            file_name=prefilled_code.file_name,
            prefilled_code_id=prefilled_code.id
        )
        return prefilled_code_dto


    def _get_prefilled_code_dtos_list(self, question: Question):
        prefilled_codes = question.prefilled_codes.all()
        prefilled_code_dtos = [
            self._get_prefilled_code_dto(prefilled_code)
            for prefilled_code in prefilled_codes
        ]
        return prefilled_code_dtos

    @staticmethod
    def _get_clean_solution_dto(clean_solution: CleanSolution):
        clean_solution_dto = CleanSolutionDto(
            language=clean_solution.language,
            solution_content=clean_solution.solution_content,
            file_name=clean_solution.file_name,
            clean_solution_id=clean_solution.id
        )
        return clean_solution_dto


    def _get_clean_solution_dtos_list(self, question: Question):
        clean_solutions = question.clean_solutions.all()
        clean_solution_dtos = [
            self._get_clean_solution_dto(clean_solution)
            for clean_solution in clean_solutions
        ]
        return clean_solution_dtos


    @staticmethod
    def _get_hint_dto(hint: Hint):
        hint_dto = HintDto(
            hint_id=hint.id,
            hint_number=hint.hint_number,
            title=hint.title,
            description=DescriptionDto(
                content=hint.content, content_type=hint.content_type
            )
        )
        return hint_dto
    
    def _get_hint_dtos_list(self, question: Question):
        hints = question.hints.all().order_by('hint_number')
        hint_dtos = [
            self._get_hint_dto(hint=hint)
            for hint in hints
        ]
        return hint_dtos
    
    @staticmethod
    def _get_solution_approach_dto(solution_approach: SolutionApproach):
        solution_approach_dto = SolutionApproachDto(
            title=solution_approach.title,
            solution_approach_id=solution_approach.id,
            description_content=solution_approach.description_content,
            description_content_type=\
                solution_approach.description_content_type,
            complexity_analysis_content=\
                solution_approach.complexity_analysis_content,
            complexity_analysis_content_type=\
                solution_approach.complexity_analysis_content_type
        )
        return solution_approach_dto


    @staticmethod
    def _get_question_dto(question: Question) -> QuestionDto:
        question_dto = QuestionDto(
            question_id=question.id,
            short_text=question.short_text,
            problem_description=DescriptionDto(
                content=question.content,
                content_type=question.content_type
            )
        )
        return question_dto
