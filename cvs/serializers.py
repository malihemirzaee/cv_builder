from rest_framework import serializers

from cvs.models import Skill, Experience, Education, Certificate, CVDetail
from users.serializers import ProfileSerializer


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        extra_kwargs = {
            'profile': {'read_only': True},
        }


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
        extra_kwargs = {
            'profile': {'read_only': True},
        }


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        extra_kwargs = {
            'profile': {'read_only': True},
        }


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"
        extra_kwargs = {
            'profile': {'read_only': True},
        }
