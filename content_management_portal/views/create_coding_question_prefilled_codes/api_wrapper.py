import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.create_prefilled_codes_interactor\
    import CreatePrefilledCodesInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = kwargs['question_id']
    prefilled_codes = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    prefilled_code_storage = \
        PrefilledCodeStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreatePrefilledCodesInteractor(
        problem_statement_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    response = interactor.create_prefilled_codes(
        question_id=question_id, prefilled_codes=prefilled_codes
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)
