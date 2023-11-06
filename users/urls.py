from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserCreateAPIView, UserDeleteAPIView, UserDetailAPIView

from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete'),
    path('view/<int:pk>/', UserDetailAPIView.as_view(), name='view'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
