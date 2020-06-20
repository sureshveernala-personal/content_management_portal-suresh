from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import Dict, Optional
from content_management_portal.dtos.dtos import DescriptionDto
from content_management_portal.interactors.mixins.question_validation_mixin \
    import QuestionValidationMixin
from content_management_portal.exceptions.exceptions import InvalidQuestionId


class CreateProblemStatementInteractor(QuestionValidationMixin):
    def __init__(
            self,
            question_storage: QuestionStorageInterface,
        ):
        self.question_storage = question_storage
    
    
    def create_problem_statement_wrapper(
            self,
            user_id: int,
            short_text: str,
            description_dto: DescriptionDto,
            question_id: Optional[None],
            presenter: PresenterInterface
        ):
        try:
            question_dto = self.create_problem_statement(
                user_id=user_id, short_text=short_text,
                description_dto=description_dto, question_id=question_id
            )
        except InvalidQuestionId:
            presenter.raise_invalid_question_id_exception()

        response = presenter.get_create_problem_statement_response(
                question_dto=question_dto
            )
        return response


    def create_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description_dto: DescriptionDto,
            question_id: Optional[None],
        ) -> int:
        # description_dto = DescriptionDto(
        #     content=description['content'],
        #     content_type=description['content_type']
        # )
        is_update = question_id is not None
        if is_update:
            question_dto = \
                self._update_problem_statement(
                    user_id=user_id,
                    short_text=short_text,
                    description=description_dto,
                    question_id=question_id
                )
        else:
            question_dto =\
            self.question_storage.create_problem_statement(
                user_id=user_id,
                short_text=short_text,
                description=description_dto
            )
        return question_dto


    def _update_problem_statement(
            self,
            user_id: int,
            short_text: str,
            description: DescriptionDto,
            question_id: int
        ):
        self._validate_question_id(question_id=question_id)

        new_question_id = self.question_storage.update_problem_statement(
            user_id=user_id,
            short_text=short_text,
            description=description,
            question_id=question_id
        )
        return new_question_id
