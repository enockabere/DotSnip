from django.contrib import admin
from authentication.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here


admin.site.register(MyUser)
