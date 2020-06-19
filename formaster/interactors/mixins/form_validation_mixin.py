from formaster.exceptions.exceptions import InvalidFormId, FormClosed


class FormValidationMixin:

    def _validate_form_id(self, form_id: int):
        is_valid_form_id = self.storage.is_valid_form_id(form_id=form_id)
        is_invalid_form_id = not is_valid_form_id
        if is_invalid_form_id:
            raise InvalidFormId


    def _validate_for_live_form(self, form_id: int):
        is_live = self.storage.is_form_live(form_id=form_id)
        is_closed = not is_live
        if is_closed:
            raise FormClosed


    def _validate_form(self, form_id: int):
        form_dto = self.storage.get_form(form_id=form_id)
        is_closed = not form_dto.is_live
        if is_closed:
            raise FormClosed
