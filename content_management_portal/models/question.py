from django.db import models
from content_management_portal.constants.enums import DescriptionType


class Question(models.Model):
    created_by_id = models.IntegerField()
    short_text = models.CharField(max_length=100)
    content = models.TextField()
    choices = [
        (description.value, description.value)
        for description in DescriptionType
    ]
    content_type = models.CharField(max_length=100, choices=choices)
    created_at = models.DateTimeField(auto_now=True)
