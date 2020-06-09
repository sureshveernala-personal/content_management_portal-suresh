from django.db import models
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import Question
from content_management_portal.constants.enums import DescriptionType


class Hint(models.Model):
    question = models.ForeignKey(
        Question, related_name="hints", on_delete = models.CASCADE
    )
    hint_number = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    choices = [
        (description.value, description.value)
        for description in DescriptionType
    ]
    content_type = models.CharField(max_length=100, choices=choices)
    created_at = models.DateTimeField(auto_now=True)
