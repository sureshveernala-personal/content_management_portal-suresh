from content_management_portal_auth.interactors.storages.user_storage_interface import\
    UserStorageInterface
from content_management_portal_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import\
    OAuthUserAuthTokensService
from content_management_portal_auth.exceptions.exceptions import InvalidPassword


class LoginInteractor:

    def __init__(
            self,
            user_storage: UserStorageInterface,
            presenter: PresenterInterface,
            oauth2_storage: OAuth2SQLStorage
        ):
        self.user_storage = user_storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage


    def login(self, username: str, password: str):
        is_valid_username = self.user_storage.is_valid_username(
            username=username
        )
        is_not_valid_username = not is_valid_username
        if is_not_valid_username:
            self.presenter.raise_invalid_username_exception()
            return

        try:
            user_id = self.user_storage.validate_password(
                username=username, password=password
            )
        except InvalidPassword:
            self.presenter.raise_invalid_password_exception()
            return

        token_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )
        access_token = token_service.create_user_auth_tokens(user_id=user_id)
        response = self.presenter.login_response(access_token)
        return response
