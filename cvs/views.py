from rest_framework import viewsets, status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from cvs.models import Skill, Experience, Education, Certificate
from cvs.serializers import SkillSerializer, ExperienceSerializer, EducationSerializer, CertificateSerializer
from users.models import Profile


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    model_cls = Skill
    queryset = Skill.objects.all()

    def perform_create(self, serializer):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Response(
                {"profile": "first complete profile"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(
            profile=profile,
        )


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExperienceSerializer
    model_cls = Experience
    queryset = Experience.objects.all()

    def perform_create(self, serializer):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Response(
                {"profile": "first complete profile"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(
            profile=profile,
        )


class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer
    model_cls = Education
    queryset = Education.objects.all()

    def perform_create(self, serializer):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Response(
                {"profile": "first complete profile"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(
            profile=profile,
        )


class CertificateViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CertificateSerializer
    model_cls = Certificate
    queryset = Certificate.objects.all()

    def perform_create(self, serializer):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Response(
                {"profile": "first complete profile"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(
            profile=profile,
        )
