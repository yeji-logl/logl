from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AuthUser, UserAvatar, Regions, UserRegion


@admin.register(AuthUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "email",
        "username",
        "username_local",
        "main_local_region",
        "main_global_region",
        "gender_code",
        "native_language",
        "birth_date",
        "marketing_consent",
    ]
    fieldsets = (
        (
            "profile",
            {
                "fields": (
                    "profile_thumbnail_url",
                    "username_local",
                    "main_local_region",
                    "main_global_region",
                    "gender_code",
                    "birth_date",
                    "native_language",
                )
            },
        ),
        (
            "marketing",
            {
                "fields": ("marketing_consent",),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse"),
            },
        ),
        (
            "important dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse"),
            },
        ),
    )


@admin.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "file_path",
        "is_primary",
        "created_at",
    ]

    list_filter = ("user", "is_primary")


@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "level",
        "parent_id",
    ]

    search_fields = ("code", "level", "parent_id", "ko", "en", "ja")


@admin.register(UserRegion)
class UserRegionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "region",
        "region_type",
        "occupation_type",
    ]

    list_filter = ("user", "region", "region_type", "occupation_type")

    search_fields = ("user", "region", "region_type", "occupation_type", "occupation_detail")