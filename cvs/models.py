from django.db import models

from users.models import Profile


class CVDetail(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Skill(CVDetail):
    BEGINNER = 3
    MIDDLE = 2
    PROFESSIONAL = 1
    LEVEL_CHOICES = [
        (BEGINNER, "beginner"),
        (MIDDLE, "middle"),
        (PROFESSIONAL, "professional")]

    skill_level = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES, default=MIDDLE
    )


class Experience(CVDetail):
    company = models.CharField(max_length=100)


class Education(CVDetail):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)


class Certificate(CVDetail):
    institution = models.CharField(max_length=100)
