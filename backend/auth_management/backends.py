from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

AuthUser = get_user_model()

class EmailBackend(ModelBackend):
    """
    Email로 로그인하도록 설정
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = AuthUser.objects.get(email=username)
        except AuthUser.DoesNotExist:
            return None

        # 비밀번호 확인 및 사용자 인증 여부 확인
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    
    def get_user(self, user_id):
        try:
            return AuthUser.objects.get(pk=user_id)
        except AuthUser.DoesNotExist:
            return None