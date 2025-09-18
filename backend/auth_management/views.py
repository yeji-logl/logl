import jwt
import requests
from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework import exceptions
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import AuthUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer


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

    permission_classes = [AllowAny]

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


class SignInJWT(APIView):
    """
    클라이언트 로그인 요청 시 토큰(access token /refresh token) 발급
    POST /api/v1/users/sign-in-jwt
    Content-Type: application/json
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            # 1. 사용자 인증
            user = authenticate(
                request,
                username=email,
                password=password,
            )

            if not user:
                raise exceptions.AuthenticationFailed("Invalid email or password")

            # 토큰 발급
            # python 코드에서 직접 RefreshToken 객체를 발급
            # = TokenObtainPairView 와 동일한 로직
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(access),
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KakaoLogin(APIView):
    """
    Kakao login
    POST: Kakao login
    URL: /api/v1/users/kakao/login
    """

    permission_classes = [AllowAny]

    def post(self, request):
        kakao_access_token = request.data.get("kakao_access_token")
        headers = {
            "Authorization": f"Bearer {kakao_access_token}",
            "Content-Type": "application/json",
        }

        # kakao 사용자 정보 요청
        kakao_response = requests.get(
            "https://kapi.kakao.com/v2/user/me", headers=headers
        )

        if kakao_response.status_code != 200:
            raise exceptions.AuthenticationFailed("Invalid kakao access token")

        data = kakao_response.json()
        kakao_email = data.get("kakao_account").get("email")



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


class CheckUsernameView(APIView):
    """
    Check username
    GET: Check username
    URL: /api/v1/users/<str:username>/check
    """

    permission_classes = [AllowAny]

    def get(self, request, username):
        exists = AuthUser.objects.filter(username=username).exists()
        return Response(
            {"username": username, "available": not exists},
            status=status.HTTP_200_OK,
        )

