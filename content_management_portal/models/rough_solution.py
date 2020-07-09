from django.db import models
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import Question
from django.contrib import admin


class RoughSolution(models.Model):
    choices = [
        (code_language.value, code_language.value)
        for code_language in CodeLanguage
    ]
    question = models.ForeignKey(
        Question, related_name="rough_solutions", on_delete = models.CASCADE
    )
    language = models.CharField(max_length=100, choices=choices)
    solution_content = models.TextField()
    file_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)


class RoughSolutionAdmin(admin.ModelAdmin):
    list_display = ('question',)