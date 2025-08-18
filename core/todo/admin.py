from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin View for"""

    list_display = (
        "id",
        "user",
        "title",
        "complete",
    )
    list_filter = (
        "user",
        "title",
        "complete",
    )
    raw_id_fields = ("user",)
    search_fields = (
        "user",
        "title",
    )
    ordering = ("user",)
