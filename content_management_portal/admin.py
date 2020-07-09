# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from content_management_portal.models import User, Person, PersonAdmin, RoughSolution, RoughSolutionAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(RoughSolution, RoughSolutionAdmin)