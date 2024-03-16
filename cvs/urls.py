from django.urls import path
from rest_framework.routers import DefaultRouter

from cvs.views import SkillViewSet, ExperienceViewSet, EducationViewSet, CertificateViewSet

router = DefaultRouter()
router.register('skill', SkillViewSet, "skill")
router.register('experience', ExperienceViewSet, "experience")
router.register('education', EducationViewSet, "education")
router.register('certificate', CertificateViewSet, "certificate")

urlpatterns = router.urls
