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
from content_management_portal.interactors.delete_rough_solution_interactor\
    import DeleteRoughSolutionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = kwargs['question_id']
    rough_solution_id = kwargs['rough_solution_id']
    question_storage = QuestionStorageImplementation()
    rough_solution_storage = \
        RoughSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteRoughSolutionInteractor(
        problem_statement_storage=question_storage, presenter=presenter,
        rough_solution_storage=rough_solution_storage
    )
    response = interactor.delete_rough_solution(
        question_id=question_id, rough_solution_id=rough_solution_id
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
