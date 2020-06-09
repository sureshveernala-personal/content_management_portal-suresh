import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.swap_hints_interactor import\
    SwapHintsInteractor
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.storages.question_storage_implementation \
    import QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    question_id = kwargs['question_id']
    hints_swap_details =kwargs['request_data']
    hint_storage = HintStorageImplementation()
    presenter = PresenterImplementation()
    question_storage = QuestionStorageImplementation()
    interactor = SwapHintsInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    response = interactor.swap_hints(
        question_id=question_id,
        hints_swap_details=hints_swap_details
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
