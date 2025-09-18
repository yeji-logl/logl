from rest_framework import serializers
from .models import Regions

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = "__all__"

class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        exclude = ("en", "ja")