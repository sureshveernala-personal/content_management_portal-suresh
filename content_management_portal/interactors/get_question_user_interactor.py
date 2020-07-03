from typing import Dict, List
from content_management_portal.interactors.storages.\
    question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from content_management_portal.exceptions.exceptions import InvalidQuestionId
from content_management_portal.adapters import service_adapter


class GetQuestionUserInteractor:

    def __init__(
            self,
            question_storage: QuestionStorageInterface,
        ):
        self.question_storage = question_storage


    def get_question_user_wrapper(
            self, question_id: int, presenter: PresenterInterface
        ):
        try:
            user_dto = self.get_question_user(question_id=question_id)
        except InvalidQuestionId:
            presenter.raise_invalid_question_id_exception()
        response = presenter.get_question_user_response(user_dto=user_dto)
        return response


    def get_question_user(self, question_id: int):
        is_invalid_question_id = not self.question_storage.\
            is_valid_question_id(question_id=question_id)
        if is_invalid_question_id:
            raise InvalidQuestionId

        user_id = self.question_storage.get_question_user_id(
            question_id=question_id
        )
        user_dto = service_adapter.get_service_adapter().\
            get_user_user_service.get_user_dtos(user_ids=[user_id])[0]
        return user_dto
