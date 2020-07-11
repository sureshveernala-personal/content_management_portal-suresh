from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import CreateProblemStatementPresenterInterface
from typing import Dict, Optional
from content_management_portal.dtos.dtos import QuestionDto


class CreateProblemStatementInteractor:
    def __init__(
            self,
            question_storage: QuestionStorageInterface,
            presenter: CreateProblemStatementPresenterInterface
        ):
        self.question_storage = question_storage
        self.presenter = presenter


    def create_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: Dict,
            question_id: Optional[None],
        ) -> int:
        question_dto = QuestionDto(
            short_text=short_text,
            content=description['content'],
            content_type=description['content_type'],
            question_id=question_id
        )
        is_update = question_id is not None
        if is_update:
            new_question_dto = \
                self._update_problem_statement(
                    user_id=user_id, question_dto=question_dto
                )
        else:
            new_question_dto = \
            self.question_storage.create_problem_statement(
                user_id=user_id, question_dto=question_dto
            )
        question_dict =\
        self.presenter.get_create_problem_statement_response(
            question_dto=new_question_dto
        )
        return question_dict


    def _update_problem_statement(
            self, user_id: int, question_dto: QuestionDto
        ):
        is_question_exists = \
        self.question_storage.is_valid_question_id(
            question_id=question_dto.question_id
        )
        if is_question_exists:
            new_question_id = \
            self.question_storage.update_problem_statement(
                user_id=user_id, question_dto=question_dto
            )
        else:
            return self.presenter.raise_invalid_question_id_exception()
        return new_question_id
