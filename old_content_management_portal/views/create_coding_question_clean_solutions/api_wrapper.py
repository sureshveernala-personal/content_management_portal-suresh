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
from content_management_portal.interactors.create_clean_solutions_interactor\
    import CreateCleanSolutionsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = kwargs['question_id']
    clean_solutions = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    clean_solution_storage = \
        CleanSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateCleanSolutionsInteractor(
        problem_statement_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    response = interactor.create_clean_solutions(
        question_id=question_id, clean_solutions=clean_solutions
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)
