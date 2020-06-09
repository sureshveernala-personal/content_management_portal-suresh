import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.rough_solution_storage_implementation \
    import RoughSolutionStorageImplementation
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.create_rough_solutions_interactor\
    import CreateRoughSolutionsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = kwargs['question_id']
    rough_solutions = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    rough_solution_storage = \
        RoughSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_solution_storage=rough_solution_storage
    )
    response = interactor.create_rough_solutions(
        question_id=question_id, rough_solutions=rough_solutions
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)
