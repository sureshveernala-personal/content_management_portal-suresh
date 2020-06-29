from abc import ABC
from abc import abstractmethod
from typing import List


class PresenterInterface(ABC):
    @abstractmethod
    def raise_invalid_username_exception(self):
        pass


    @abstractmethod
    def raise_invalid_password_exception(self):
        pass


    @abstractmethod
    def login_response(self, access_token):
        pass
