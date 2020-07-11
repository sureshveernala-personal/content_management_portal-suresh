from content_management_portal.constants.exception_messages import\
    INVALID_QUESTION_ID
from django_swagger_utils.drf_server.exceptions import NotFound
import json
from django.http import response


class QuestionValidationMixin:

    def raise_invalid_question_id_exception(self) -> response.HttpResponse:
        data = json.dumps(
            {
                "response": INVALID_QUESTION_ID[0],
                "http_status_code": 404,
                "res_status": INVALID_QUESTION_ID[1]
            }
        )
        return response.HttpResponse(data, status=404)
