from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Regions
from . import serializers
from rest_framework.response import Response
from rest_framework import status

class RegionsView(APIView):
    """
    Regions
    GET: Regions
    POST: Regions (운영자용)
    URL: /api/v1/users/regions
    queryParams:?level=0&parent_id=0
    """
    permission_classes = [AllowAny]
    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     elif self.request.method == "POST":
    #         return [IsAdminUser()]
    #     return super().get_permissions()

    def get(self, request):
        regions = Regions.objects.all()
        
        # 각 파라미터가 존재할 때만 필터링
        if 'level' in request.query_params:
            regions = regions.filter(level=int(request.query_params['level']))
        
        if 'parent_id' in request.query_params:
            regions = regions.filter(parent_id=int(request.query_params['parent_id']))
            
        serializer = serializers.RegionsSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 운영자 관리용
    def post(self, request):
        serializer = serializers.RegionsSerializer(data=request.data)
        if serializer.is_valid():
            region = serializer.save()
            serializer = serializers.RegionsSerializer(region)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionDetailView(APIView):
    """
    Region Detail
    GET: Region Detail
    URL: /api/v1/users/regions/<str:code>
    """
    permission_classes = [AllowAny]
    def get(self, request, code):
        region = Regions.objects.get(code=code)
        serializer = serializers.RegionsSerializer(region)
        return Response(serializer.data, status=status.HTTP_200_OK)
