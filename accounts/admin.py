from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForms
from django.contrib.auth.models import Group

User = get_user_model()

# Register your models here.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForms

    list_display = ('name', 'phone_number', 'email',
                    'is_active', 'is_admin', 'is_staff')
    list_filter = ('is_admin',)

    fieldsets = (
        (
            None, {
                'fields': ('name', 'phone_number', 'email', 'password')
            }
        ),
        (
            'permissions', {
                'fields': ('is_admin', 'is_staff')
            }
        )
    )

    add_fieldsets = (
        (
            None, {
                'fields': ('name', 'phone_number', 'email', 'is_active', 'password1', 'password2')
            }
        ),
        ('permissions', {'fields': ('is_admin', 'is_staff')})
    )
    ordering = ('name',)
    search_fields = ('name',)
    filter_horizontal=()


admin.site.register(User, UserAdmin)
