from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserTable

from django.contrib import admin


# Register your models here.

class UserTableAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'user', 'isprofessor', 'university']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

#admin.site.register(UserTable)

admin.site.register(UserTable, UserTableAdmin)