import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.get_questions_interactor\
    import GetQuestionsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    query_parameters = kwargs['request_query_params']
    offset = query_parameters['offset']
    limit = query_parameters['limit']
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetQuestionsInteractor(
        question_storage=question_storage, presenter=presenter
    )
    response = interactor.get_questions(offset=offset, limit=limit)
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
