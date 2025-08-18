from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ["email", "is_staff", "is_active"]
    search_fields = ["email"]
    ordering = ["email"]
    # for show fields
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
        (
            "Group Permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "Important Date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    # for add new user from admin panel
    add_fieldsets = (
        (
            "Authentication",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            "group permissions",
            {
                "classes": ("wide",),
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "classes": ("wide",),
                "fields": ("last_login",),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)