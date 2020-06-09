import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.swap_test_cases_interactor import\
    SwapTestCasesInteractor
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation
from content_management_portal.storages.question_storage_implementation \
    import QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    question_id = kwargs['question_id']
    test_cases_swap_details =kwargs['request_data']
    test_case_storage = TestCaseStorageImplementation()
    presenter = PresenterImplementation()
    question_storage = QuestionStorageImplementation()
    interactor = SwapTestCasesInteractor(
        test_case_storage=test_case_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    response = interactor.swap_test_cases(
        question_id=question_id,
        test_cases_swap_details=test_cases_swap_details
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
