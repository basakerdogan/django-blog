from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import custom_user_model

# Register your models here.
@admin.register(custom_user_model)
class custom_admin(UserAdmin):
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (('avatar change',{'fields':['avatar']}),)
