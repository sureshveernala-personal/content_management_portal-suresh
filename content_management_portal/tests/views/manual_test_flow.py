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


    # creating questions
    data = '{"question_id": null,"short_text": "string","problem_description": {"content": "string", "content_type": "TEXT"}}'
    question_id_json = requests.post(
        url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    data = '{"question_id": null,"short_text": "string","problem_description": {"content": "string", "content_type": "TEXT"}}'
    requests.post(
        url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    )


    # home page display 1 question
    parameters = {"offset": 1, "limit": 1}
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
    assert len(questions_list) == 1
    print("homepage with questions: ", json.loads(questions))
    print()

    question_id_dict = json.loads(question_id_json)
    question_id = question_id_dict['question_id']

    #update question
    data = {"question_id": question_id,"short_text": "update","problem_description": {"content": "update", "content_type": "TEXT"}}
    data = json.dumps(data)
    requests.post(
        url='http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    )

    # home page display 1 question updated
    parameters = {"offset": 1, "limit": 1}
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
    assert len(questions_list) == 1
    print("homepage updated question: ", json.loads(questions))
    print()
    question_id_dict = json.loads(question_id_json)
    question_id = question_id_dict['question_id']


    # no rough status
    assert questions_list[0]['rough_solution_status'] == False


    # get question details

    question_details = requests.get(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        }
    )
    assert question_details.status_code == 200
    print("question_details:", json.loads(question_details.content))
    print()


    # creating rough solutions
    data = '[{"language":"JAVA","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    rough_solutions_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solutions/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content


    # home page
    parameters = {"offset": 1, "limit": 2}
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
    assert len(questions_list) == 2
    print("home_page rough solution True:", json.loads(questions))
    print()


    # rough solution status
    assert questions_list[0]['rough_solution_status'] == True
    assert questions_list[1]['rough_solution_status'] == False


    rough_solutions = json.loads(
        rough_solutions_with_question_id
    )['rough_solutions']
    rough_solution_id = rough_solutions[0]['rough_solution_id']

    # update rough solutions
    data = [{"language":"C","solution_content":"update","file_name":"update","rough_solution_id": rough_solution_id}]
    data =json.dumps(data)
    print("before_update:", rough_solutions_with_question_id)
    print()
    rough_solutions_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solutions/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("after_update:", rough_solutions_with_question_id)
    print()


    # delete rough solution
    # requests.delete(
    #     url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solutions/{rough_solution_id}/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # )


    # homepage after deleting rough solution
    # parameters = {"offset": 1, "limit": 2}
    # questions = requests.get(
    #     url='http://localhost:8080/api/content_management_portal/coding_questions/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=user_data,
    #     params=parameters
    # ).content
    # questions_dict = json.loads(questions)
    # questions_list = questions_dict['questions_list']
    # assert len(questions_list) == 2
    # print("home_page no rough solution:", json.loads(questions))
    # print()

    ################
    #create clean solution
    data = [
        {
            "language": "PYTHON",
            "solution_content": "string",
            "file_name": "string",
            "clean_solution_id": None
         }
    ]
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/clean_solutions/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("clean_solutions:", clean_solutions_with_question_id )
    print()
    clean_solutions = json.loads(clean_solutions_with_question_id)
    clean_solution_id  = clean_solutions['clean_solutions'][0]['clean_solution_id']


    #update clean solution
    data = [
        {
            "language": "PYTHON",
            "solution_content": "update",
            "file_name": "update",
            "clean_solution_id": clean_solution_id
         }
    ]
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/clean_solutions/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content

    print("updated clean solutions:", clean_solutions_with_question_id )
    print()
    #delete clean solution
    # data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    # data = json.dumps(data)
    # clean_solutions_with_question_id = requests.delete(
    #     url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/clean_solutions/{clean_solution_id}/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # print("delete clean solutions:", clean_solutions_with_question_id)
    # print()

    #create prefilled code
    data = [
        {
            "language": "PYTHON",
            "solution_content": "string",
            "file_name": "string",
            "prefilled_code_id": None
        }
    ]
    data = json.dumps(data)
    prefilled_codes_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/prefilled_codes/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create prefilled codes:", prefilled_codes_with_question_id )
    print()
    prefilled_codes = json.loads(prefilled_codes_with_question_id)
    prefilled_code_id  = prefilled_codes['prefilled_codes'][0]['prefilled_code_id']


    #update prefilled code
    data = data = [
        {
            "language": "PYTHON",
            "solution_content": "update",
            "file_name": "update",
            "prefilled_code_id": prefilled_code_id
        }
    ]
    data = json.dumps(data)
    prefilled_codes_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/prefilled_codes/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content

    print("updated prefilled codes:", prefilled_codes_with_question_id )
    print()

    #delete prefilled code
    # data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    # data = json.dumps(data)
    # clean_solutions_with_question_id = requests.delete(
    #     url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/prefilled_codes/{prefilled_code_id}/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # print("delete clean solution:", clean_solutions_with_question_id )
    # print()


    #create test case
    data = {
        "test_case_number": 1,
        "input": "string",
        "output": "string",
        "score": 0,
        "is_hidden": True,
        "test_case_id": None
    }
    data = json.dumps(data)
    test_case_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create test case:", test_case_with_question_id )
    print()
    test_case = json.loads(test_case_with_question_id)
    test_case_id  = test_case['test_case']['test_case_id']


    #update test case
    data = {
        "test_case_number": 1,
        "input": "update",
        "output": "update",
        "score": 0,
        "is_hidden": True,
        "test_case_id": test_case_id
    }
    data = json.dumps(data)
    test_case_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content

    print("updated test case:", test_case_with_question_id )
    print()



    #delete test case
    # data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    # data = json.dumps(data)
    # clean_solutions_with_question_id = requests.delete(
    #     url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/{test_case_id}/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # print("delete test case:", clean_solutions_with_question_id )
    # print()

    #create hint
    data = {
        "title": "string",
        "description": {
            "content": "string",
            "content_type": "TEXT"
        },
        "hint_number": 1,
        "hint_id": None
    }
    data = json.dumps(data)
    hint_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create hint:", hint_with_question_id )
    print()
    hint = json.loads(hint_with_question_id)
    hint_id  = hint['hint']['hint_id']


    #update hint
    data = {
        "title": "update",
        "description": {
            "content": "update",
            "content_type": "TEXT"
        },
        "hint_number": 2,
        "hint_id": hint_id
    }
    data = json.dumps(data)
    hint_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content

    print("updated hints:", hint_with_question_id )
    print()



    #delete hint
    # data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    # data = json.dumps(data)
    # hint_with_question_id = requests.delete(
    #     url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/{hint_id}/v1/',
    #     headers={
    #         "content-type":"application/json",
    #         "Authorization": f"Bearer {access_token}"
    #     },
    #     data=data
    # ).content
    # print("delete hint:", hint_with_question_id )

    #create solution approach
    data = {
        "title": "string",
        "description": {
            "content": "string",
            "content_type": "TEXT"
        },
          "complexity_analysis": {
            "content": "string",
            "content_type": "TEXT"
        },
        "solution_approach_id": None
    }
    data = json.dumps(data)
    solution_approach_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/solution_approaches/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create solution approach:", solution_approach_with_question_id )
    print()
    solution_approach = json.loads(solution_approach_with_question_id)
    solution_approach_id  = solution_approach['solution_approach']['solution_approach_id']

    #update solution approach
    data = {
        "title": "update",
        "description": {
            "content": "update",
            "content_type": "TEXT"
        },
          "complexity_analysis": {
            "content": "update",
            "content_type": "TEXT"
        },
        "solution_approach_id": solution_approach_id
    }
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/solution_approaches/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content

    print("updated solution approach:", clean_solutions_with_question_id )
    print()

    question_details = requests.get(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        }
    )
    assert question_details.status_code == 200
    print("question_details:", json.loads(question_details.content))
    print()

    # home page
    parameters = {"offset": 1, "limit": 1}
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
    assert len(questions_list) == 1
    print("home_page all True:", json.loads(questions))
    print()


    #delete rough solutions
    requests.delete(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solutions/{rough_solution_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    )

    # delete clean solution
    data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.delete(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/clean_solutions/{clean_solution_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("delete clean solutions:", clean_solutions_with_question_id)
    print()

    # delete prefilled code
    data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.delete(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/prefilled_codes/{prefilled_code_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("delete clean solution:", clean_solutions_with_question_id )
    print()

    # delete test case
    data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    data = json.dumps(data)
    clean_solutions_with_question_id = requests.delete(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/{test_case_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("delete test case:", clean_solutions_with_question_id )
    print()

    # delete hint
    data = '[{"language":"C","solution_content":"string","file_name":"string","rough_solution_id": null}]'
    data = json.dumps(data)
    hint_with_question_id = requests.delete(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/{hint_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("delete hint:", hint_with_question_id )
    print()

    # home page
    parameters = {"offset": 1, "limit": 1}
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
    assert len(questions_list) == 1
    print("home_page all False except solution approach:", json.loads(questions))
    print()


        #for swapping

    #create hint
    data = {
        "title": "string",
        "description": {
            "content": "string",
            "content_type": "TEXT"
        },
        "hint_number": 1,
        "hint_id": None
    }
    data = json.dumps(data)
    hint_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create hint:", hint_with_question_id )
    hint = json.loads(hint_with_question_id)
    first_hint_id  = hint['hint']['hint_id']

    #create hint
    data = {
        "title": "string",
        "description": {
            "content": "string",
            "content_type": "TEXT"
        },
        "hint_number": 2,
        "hint_id": None
    }
    data = json.dumps(data)
    hint_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create hint:", hint_with_question_id )
    hint = json.loads(hint_with_question_id)
    second_hint_id  = hint['hint']['hint_id']

    #create test case
    data = {
        "test_case_number": 1,
        "input": "string",
        "output": "string",
        "score": 0,
        "is_hidden": True,
        "test_case_id": None
    }
    data = json.dumps(data)
    test_case_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create test case:", test_case_with_question_id )
    print()
    test_case = json.loads(test_case_with_question_id)
    first_test_case_id  = test_case['test_case']['test_case_id']

    #create test case
    data = {
        "test_case_number": 2,
        "input": "string",
        "output": "string",
        "score": 0,
        "is_hidden": True,
        "test_case_id": None
    }
    data = json.dumps(data)
    test_case_with_question_id = requests.post(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    ).content
    print("create test case:", test_case_with_question_id )
    print()
    test_case = json.loads(test_case_with_question_id)
    second_test_case_id  = test_case['test_case']['test_case_id']




    question_details = requests.get(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        }
    )
    assert question_details.status_code == 200
    print("before swapping question_details:", json.loads(question_details.content))
    print()

    #swap hint
    data = {
        "first_hint": {
            "hint_id": first_hint_id,
            "hint_number": 1
        },
        "second_hint": {
            "hint_id": second_hint_id,
            "hint_number": 2
        }
    }
    data = json.dumps(data)
    requests.put(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/hints/swap/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    )

    #swap test case
    data = {
          "first_test_case": {
            "test_case_id": first_test_case_id,
            "test_case_number": 1
          },
          "second_test_case": {
            "test_case_id": second_test_case_id,
            "test_case_number": 2
          }
    }
    data = json.dumps(data)
    requests.put(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/test_cases/swap/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=data
    )

    question_details = requests.get(
        url=f'http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/',
        headers={
            "content-type":"application/json",
            "Authorization": f"Bearer {access_token}"
        }
    )
    assert question_details.status_code == 200
    print("after swapping question_details:", json.loads(question_details.content))
    print()



manual_test_flow_of_operations()