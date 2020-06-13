from django.db import models
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.models import Question
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_postive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an postive number'),
            params={'value': value},
        )

class TestCase(models.Model):
    question = models.ForeignKey(
        Question, related_name="test_cases", on_delete = models.CASCADE
    )
    test_case_number = models.IntegerField()
    input = models.TextField()
    output = models.TextField()
    score = models.IntegerField(validators=[validate_postive])
    is_hidden = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

