from formaster.exceptions.exceptions import InvalidQuestionId,\
    QuestionIdNotBelongsToForm


class QuestionValidationMixin:

    def _validate_question_id(self, question_id: int):
        is_valid_question_id = self.storage.is_valid_question_id(
            question_id=question_id
        )
        is_invalid_question_id = not is_valid_question_id
        if is_invalid_question_id:
            raise InvalidQuestionId


    def _validate_question_id_with_form(self, question_id: int, form_id: int):
        is_question_id_belongs_form = self.storage.is_question_id_belongs_form(
            question_id=question_id, form_id=form_id
        )
        is_question_id_not_belongs_form = not is_question_id_belongs_form
        if is_question_id_not_belongs_form:
            raise QuestionIdNotBelongsToForm
