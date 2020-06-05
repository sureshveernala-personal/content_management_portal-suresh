import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.create_problem_statement_interactor\
    import CreateProblemStatementInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']
    question_id = request_data['question_id']
    short_text = request_data['short_text']
    description = request_data['problem_description']
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateProblemStatementInteractor(
        problem_statement_storage=question_storage, presenter=presenter
    )
    response = interactor.create_problem_statement(
        user_id=user.id,
        short_text=short_text,
        description=description,
        question_id=question_id
    )
    
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)
