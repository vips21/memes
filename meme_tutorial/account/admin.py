from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('accept_cookie',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('accept_cookie',)}),
    )
    # fieldsets = UserAdmin.fieldsets

admin.site.register(User, CustomUserAdmin)
