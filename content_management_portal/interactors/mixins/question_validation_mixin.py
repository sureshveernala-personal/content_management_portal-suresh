from content_management_portal.exceptions.exceptions import InvalidQuestionId
class QuestionValidationMixin:

    def _validate_question_id(self, question_id: int):
        is_question_exists = \
        self.question_storage.is_valid_question_id(question_id=question_id)
        is_question_not_exists = not is_question_exists
        if is_question_not_exists:
            raise InvalidQuestionId
