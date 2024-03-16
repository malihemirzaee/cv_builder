from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        try:
            validate_password(validated_data.get("password"))
        except ValidationError as exc:
            raise serializers.ValidationError(exc.messages)
        user = User.objects.create_user(
            username=validated_data.get("username")
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return validated_data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }


