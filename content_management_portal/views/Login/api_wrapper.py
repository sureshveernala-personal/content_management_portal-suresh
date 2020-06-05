import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.user_storage_implementation import\
    UserStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.login_interactor\
    import LoginInteractor
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    user_storage = UserStorageImplementation()
    oauth2_storage = OAuth2SQLStorage()
    presenter = PresenterImplementation()
    interactor = LoginInteractor(
        user_storage=user_storage, presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    response = interactor.login(username=username, password=password)
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)
