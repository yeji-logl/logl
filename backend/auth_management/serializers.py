from typing import Required
from rest_framework import serializers
from .models import AuthUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = (
            "id",
            "uid",
            "password",
            "email",
            "username",
            "gender_code",
            "birth_date",
            "native_language",
            "date_joined",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)