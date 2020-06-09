import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.get_question_details_interactor\
    import GetQuestionDetailsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id=kwargs['question_id']
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetQuestionDetailsInteractor(
        question_storage=question_storage, presenter=presenter
    )
    response = interactor.get_question_details(question_id=question_id)
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
