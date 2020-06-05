import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.storages.clean_solution_storage_implementation \
    import CleanSolutionStorageImplementation
from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation
from content_management_portal.interactors.delete_clean_solution_interactor\
    import DeleteCleanSolutionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = kwargs['question_id']
    clean_solution_id = kwargs['clean_solution_id']
    question_storage = QuestionStorageImplementation()
    clean_solution_storage = \
        CleanSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteCleanSolutionInteractor(
        problem_statement_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    response = interactor.delete_clean_solution(
        question_id=question_id, clean_solution_id=clean_solution_id
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
