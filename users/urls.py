from django.urls import path
from .views import UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #로그인 시 사용하는 API : (접근토큰과 리프레쉬) 토큰 발급
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'), #토큰 새로 발급해주는 API : 리프레쉬 토큰을 바탕으로 접근 토큰 새로 발급해 줌
]
