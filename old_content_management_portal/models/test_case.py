from django.db import models
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import Question


class TestCase(models.Model):
    question = models.ForeignKey(
        Question, related_name="test_cases", on_delete = models.CASCADE
    )
    test_case_number = models.IntegerField()
    input = models.TextField()
    output = models.TextField()
    score = models.IntegerField()
    is_hidden = models.BooleanField()
