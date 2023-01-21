from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm
from . import models


class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form= CustomUserChangeForm
    model= models.CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ] 
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
    (None, {'fields': ('age',)}),
    )


# Register your models here.
admin.site.register(models.CustomUser, CustomUserAdmin)