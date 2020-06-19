from formaster.exceptions.exceptions import InvalidUserResponse


class OptionValidationMixin:

    def _validate_option_id_with_question(
            self, question_id: int, option_id: int
        ):
        is_option_id_belongs_to_question = \
            self.storage.is_option_id_belongs_to_question(
                question_id=question_id, option_id=option_id
            )
        is_option_id_not_belongs_to_question = \
            not is_option_id_belongs_to_question
        if is_option_id_not_belongs_to_question:
            raise InvalidUserResponse
