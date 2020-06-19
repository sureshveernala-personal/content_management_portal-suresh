from abc import abstractmethod
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.mixins.form_validation_mixin import \
    FormValidationMixin
from formaster.interactors.mixins.question_validation_mixin import\
    QuestionValidationMixin
from formaster.exceptions.exceptions import InvalidFormId, FormClosed,\
    InvalidQuestionId, QuestionIdNotBelongsToForm, InvalidUserResponse


class BaseSubmitFormResponseInteractor(
        FormValidationMixin, QuestionValidationMixin
    ):

    def __init__(
            self, storage: StorageInterface, user_id: int, form_id,
            question_id:int
        ):
        self.storage = storage
        self.user_id = user_id
        self.form_id = form_id
        self.question_id = question_id

    def sumbit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            response_id = self.submit_form_response()
        except InvalidFormId:
            presenter.raise_invalid_form_id_exception()
        except FormClosed:
            presenter.raise_form_closed_exception()
        except InvalidQuestionId:
            presenter.raise_invalid_question_id_exception()
        except QuestionIdNotBelongsToForm:
            presenter.raise_question_not_belongs_to_question_exception()
        except InvalidUserResponse:
            presenter.raise_invalid_user_response_exception()
        response = presenter.get_submit_form_response(response_id=response_id)
        return response


    def submit_form_response(self):
        self._validate_form(form_id=self.form_id)
        self._validate_question_id(question_id=self.question_id)
        self._validate_question_id_with_form(
            question_id=self.question_id, form_id=self.form_id
        )
        self._validate_user_response()
        response_id = self._create_user_response()
        return response_id


    @abstractmethod
    def _validate_user_response(self):
        pass


    @abstractmethod
    def _create_user_response(self) -> int:
        pass
