from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    fields = (
        "user",
        "first_name",
        "last_name",
        "age",
        "address",
    )
    list_display = ("id", "first_name", "last_name")
