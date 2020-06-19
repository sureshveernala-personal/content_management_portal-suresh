from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_form_id_exception(self):
        pass


    @abstractmethod
    def raise_form_closed_exception(self):
        pass


    @abstractmethod
    def raise_invalid_question_id_exception(self):
        pass


    @abstractmethod
    def raise_question_not_belongs_to_question_exception(self):
        pass


    @abstractmethod
    def raise_invalid_user_response_exception(self):
        pass


    @abstractmethod
    def get_submit_form_response(self, response_id: int):
        pass
