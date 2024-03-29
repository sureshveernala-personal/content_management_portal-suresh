from content_management_portal.interactors.storages.\
    problem_statement_storage_interface import ProblemStatementStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetQuestionDetailsInteractor:
    def __init__(
            self,
            problem_statement_storage: ProblemStatementStorageInterface,
            presenter: PresenterInterface
        ):
        self.problem_statement_storage = problem_statement_storage
        self.presenter = presenter

    def get_question_details(self, question_id: int):
        is_valid_question_id = self.\
            problem_statement_storage.is_valid_question_id(
                question_id=question_id
            )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            self.presenter.raise_invalid_question_id_exception()
        question_dto, rough_solution_dtos, clean_solution_dtos,\
        test_case_dtos, solution_approach_dto, hint_dtos,\
        prefilled_code_dtos = \
            self.problem_statement_storage.get_question_details(
                question_id=question_id
            )
        questions_dict = self.presenter.get_question_details_response(
            question_dto=question_dto,
            rough_solution_dtos=rough_solution_dtos,
            clean_solution_dtos=clean_solution_dtos,
            test_case_dtos=test_case_dtos,
            solution_approach_dto=solution_approach_dto,
            hint_dtos=hint_dtos,
            prefilled_code_dtos=prefilled_code_dtos
        )
        return questions_dict
