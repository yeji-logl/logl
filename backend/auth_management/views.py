from django.contrib.auth import login, logout
from rest_framework import exceptions
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import AuthUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


class Me(APIView):
    """
    User
    POST: Create a new user
    URL: /api/v1/users/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Users(APIView):
    """
    User
    POST: Create a new user
    URL: /api/v1/users/
    """

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise exceptions.ParseError("password is required")
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            raise exceptions.ParseError("email and password are required")

        user = authenticate(
            request,
            username=email,
            password=password,
        )

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise exceptions.AuthenticationFailed("Invalid email or password")


    """"
    Sign in
    POST: Sign in
    URL: /api/v1/users/sign-in
    """
""" 
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise exceptions.ParseError("username and password are required")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise exceptions.AuthenticationFailed("Invalid username or password")
"""



class SignOut(APIView):
    """
    Sign out
    POST: Sign out
    URL: /api/v1/users/sign-out
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
