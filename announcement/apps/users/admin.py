# Django
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.auth.admin import UserAdmin as _UserAdmin


# Local
from users.models import User

@admin.register(User)
class UserAdmin(_UserAdmin):
    fieldsets = (
        (_('Base'), {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'department')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_verified',
                'is_superuser', 'groups', 'user_permissions'
            )
        }),
    )

    add_fieldsets = (
       (None, {
           'fields': (
               'first_name', 'last_name', 'email', 'password1', 'password2'
           )
       }),
    )

    list_display = (
        'first_name', 'last_name', 'email', 'department',
        'is_active', 'is_verified', 'is_superuser'
    )

    list_filter = ('is_active', 'is_verified', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')
