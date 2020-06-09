from django.db import models
from content_management_portal.constants.enums import DescriptionType
from .user import User


class Question(models.Model):
    created_by = models.ForeignKey(
        User,on_delete = models.CASCADE,related_name="questions"
    )
    short_text = models.CharField(max_length=100)
    content = models.TextField()
    choices = [
        (description.value, description.value)
        for description in DescriptionType
    ]
    content_type = models.CharField(max_length=100, choices=choices)
    created_at = models.DateTimeField(auto_now=True)
