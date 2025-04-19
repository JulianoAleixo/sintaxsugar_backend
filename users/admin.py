from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    model = User
    list_display = ("email", "full_name", "is_staff", "is_active", "is_superuser", "date_joined")
    list_filter = ("is_staff", "is_active", "is_superuser")
    fieldsets = (
        (None, {"fields": ("email", "password", "full_name", "bio")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("email", "full_name")
    ordering = ("full_name", "email")
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_active")},
        ),
    )


admin.site.register(User, UserAdmin)
