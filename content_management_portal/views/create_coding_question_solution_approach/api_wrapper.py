import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.create_solution_approach_interactor import\
    CreateSolutionApproachInteractor
from content_management_portal.storages.solution_approach_storage_implementation \
    import SolutionApproachStorageImplementation
from content_management_portal.storages.question_storage_implementation \
    import QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation import\
    PresenterImplementation



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    solution_approach_details = kwargs['request_data']
    question_id = kwargs['question_id']
    solution_approach_storage = SolutionApproachStorageImplementation()
    presenter = PresenterImplementation()
    problem_statement_storage = QuestionStorageImplementation()
    interactor = CreateSolutionApproachInteractor(
        solution_approach_storage=solution_approach_storage,
        presenter=presenter,
        problem_statement_storage=problem_statement_storage
    )
    response = interactor.create_solution_approach(
        question_id=question_id,
        solution_approach_details=solution_approach_details
    )
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=201)