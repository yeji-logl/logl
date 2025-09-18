from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("sign-in", views.SignInJWT.as_view()),

    # access token / refresh token 발급 (다른 로직 필요없음 url 지정해주는 것 만으로 토큰 발급 가능)
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # refresh token 을 통해 access token 갱신
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("sign-out", views.SignOut.as_view()),
    # kakao login
    path("kakao/login/", views.KakaoLogin.as_view()),
    path("<str:username>/check/", views.CheckUsernameView.as_view()),
]   