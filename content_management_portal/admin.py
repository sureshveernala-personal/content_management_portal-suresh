# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from content_management_portal.models import User

admin.site.register(User, UserAdmin)