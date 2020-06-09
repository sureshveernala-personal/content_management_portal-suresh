from django.db import models
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import Question
from content_management_portal.constants.enums import DescriptionType


class SolutionApproach(models.Model):
    question = models.OneToOneField(
        Question, related_name="solution_approach", on_delete = models.CASCADE
    )
    choices = [
        (description.value, description.value)
        for description in DescriptionType
    ]
    title = models.CharField(max_length=100)
    description_content = models.TextField()
    description_content_type = models.CharField(
        max_length=100, choices=choices
    )
    complexity_analysis_content = models.TextField()
    complexity_analysis_content_type = models.CharField(
        max_length=100, choices=choices
    )
    created_at = models.DateTimeField(auto_now=True)
