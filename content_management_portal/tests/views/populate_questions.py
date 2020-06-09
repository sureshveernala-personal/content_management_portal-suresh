import requests
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest,\
    Forbidden
from content_management_portal.models import User, Question, RoughSolution
import json
from django.db import connection


def manual_test_flow_of_operations():

    # clearing data
    User.objects.all().delete()
    Question.objects.all().delete()

    # when no user
    user_data = '{"username":"suresh","password": "123"}'
    response = requests.post(
        url='http://localhost:8080/api/content_management_portal/login/v1/',
        headers={
            "content-type":"application/json",
        },
        data=user_data
    )
    assert response.status_code == 404


    # getting acces token
    User.objects.create_user(username="suresh", password="123")
    access_token_dto = requests.post(
        url='http://localhost:8080/api/content_management_portal/login/v1/',
        headers={
            "content-type":"application/json",
        },
        data=user_data
    ).content
    access_token_dict = json.loads(access_token_dto)
    print(access_token_dict)
    print()
    access_token = access_token_dict['access_token']


    # empty homepage
    parameters = {"offset": 1, "limit": 10}
    questions = requests.get(
        url='http://localhost:8080/api/content_management_portal/coding_questions/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=user_data,
        params=parameters
    ).content
    questions_dict = json.loads(questions)
    questions_list = questions_dict['questions_list']
    assert questions_list == []
    print("home_page empty:", json.loads(questions))


    # # creating questions
    # data = '{"question_id": null,"short_text": "question1","problem_description": {"content": "content1", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question2","problem_description": {"content": "content2", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question3","problem_description": {"content": "content3", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question4","problem_description": {"content": "content4", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question5","problem_description": {"content": "content5", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question6","problem_description": {"content": "content6", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question7","problem_description": {"content": "content7", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question8","problem_description": {"content": "content8", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question9","problem_description": {"content": "content9", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question10","problem_description": {"content": "content10", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question11","problem_description": {"content": "content", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question12","problem_description": {"content": "string", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    # data = '{"question_id": null,"short_text": "question13","problem_description": {"content": "string", "content_type": "TEXT"}}'
    # question_id_json = requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # data = '{"question_id": null,"short_text": "question14","problem_description": {"content": "string", "content_type": "TEXT"}}'
    # requests.post(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )
    for i in range(15):
        data = {
            "question_id": None,
            "short_text": f"question_{i}",
            "problem_description": 
                {"content": f"content_{i}", "content_type": "TEXT"}
        }
        data = json.dumps(data)
        requests.post(
            url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
            headers={
                "content-type":"application/json",
                "Authorization": f"Bearer {access_token}"
            },
            data=data
        )


manual_test_flow_of_operations()