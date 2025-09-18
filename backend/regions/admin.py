from django.contrib import admin
from .models import Regions

@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "level",
        "parent_id",
    ]

    search_fields = ("code", "level", "parent_id", "ko", "en", "ja")
