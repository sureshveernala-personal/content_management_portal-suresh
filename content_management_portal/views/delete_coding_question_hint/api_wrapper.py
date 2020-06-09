import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.delete_hint_interactor import\
    DeleteHintInteractor
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation
from content_management_portal.storages.question_storage_implementation \
    import QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    hint_id = kwargs['hint_id']
    question_id = kwargs['question_id']
    hint_storage = HintStorageImplementation()
    presenter = PresenterImplementation()
    question_storage = QuestionStorageImplementation()
    interactor = DeleteHintInteractor(
        hint_storage=hint_storage,
        presenter=presenter,
        question_storage=question_storage
    )
    response = interactor.delete_hint(
        question_id=question_id, hint_id=hint_id
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)