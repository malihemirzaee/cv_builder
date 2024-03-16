from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from cvs.models import Skill, Experience, Education, Certificate


@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    fields = (
        "profile",
        "title",
        "description",
        "start_date",
        "end_date",
        "skill_level",
    )
    list_display = ("id", "title")


@admin.register(Experience)
class ExperienceAdmin(ImportExportModelAdmin):
    fields = (
        "profile",
        "title",
        "description",
        "start_date",
        "end_date",
        "company",
    )
    list_display = ("id", "title")


@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin):
    fields = (
        "profile",
        "title",
        "description",
        "start_date",
        "end_date",
        "institution",
        "degree",
    )
    list_display = ("id", "title")


@admin.register(Certificate)
class CertificateAdmin(ImportExportModelAdmin):
    fields = (
        "profile",
        "title",
        "description",
        "start_date",
        "end_date",
        "institution",
    )
    list_display = ("id", "title")
