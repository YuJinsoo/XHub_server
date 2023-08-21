from django.urls import path
from .views import RegisterView, UnregisterUserView
from .views import (
    RegisterView,
    Login,
    Logout,
    Update
    )

app_name = "player"

urlpatterns = [
    # 회원가입
    path("register/", RegisterView, name="register"),

    # 로그인
    path('login/', Login, name='login'),

    # 로그아웃
    path('logout/', Logout, name='logout'),

    # 회원 정보수정
    path('update/', Update, name='update'),

    # 회원 탈퇴
    # path("<str:playerId>/", 기능, name="remove"),
    path("unregister/", UnregisterUserView.as_view(), name="unregister"),

    # 회원 조회
    # path("search/<str:playerId>/", 기능, name="search"),
]
