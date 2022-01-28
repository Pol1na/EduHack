from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields', {
                'fields': (
                    'name',
                    'surname',
                    'patronymic',
                    'username',
                    'password'
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields', {
                'fields': (
                    'name',
                    'surname',
                    'patronymic'
                )
            }
        )
    )
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # list_display = ['email', 'username', ]

# admin.site.register(CustomUser, CustomUserAdmin)
