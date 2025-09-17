from django.contrib import admin
from .models import OccupationType


@admin.register(OccupationType)
class OccupationTypeAdmin(admin.ModelAdmin):
    list_display = [
        "region_type",
        "code",
        "order",
        "is_active",
    ]

    list_filter = ("code",)