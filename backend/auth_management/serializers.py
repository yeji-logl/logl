from typing import Required
from rest_framework import serializers
from .models import AuthUser


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


""" class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    uid = serializers.UUIDField(required=True)
    profile_thumbnail_url = serializers.CharField(required=False)
    username_local = serializers.CharField(required=False)
    main_local_region_id = serializers.IntegerField(required=False)
    main_global_region_id = serializers.IntegerField(required=False)
    gender_code = serializers.ChoiceField(required=True, choices=AuthUser.GenderChoices.choices)
    birth_date = serializers.DateField(required=True)
    marketing_consent = serializers.BooleanField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    native_language = serializers.CharField(required=True)

    def create(self, validated_data) -> AuthUser:
        return AuthUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.profile_thumbnail_url = validated_data.get('profile_thumbnail_url', instance.profile_thumbnail_url)
        instance.main_local_region_id = validated_data.get('main_local_region_id', instance.main_local_region_id)
        instance.main_global_region_id = validated_data.get('main_global_region_id', instance.main_global_region_id)
        instance.marketing_consent = validated_data.get('marketing_consent', instance.marketing_consent)
        instance.save()
        return instance """
