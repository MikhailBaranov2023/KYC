from rest_framework import generics
from users.serializers import UserSerializer, CreateUserSerializer
from users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsStaffPermission, IsOwnerPermission


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class UserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerPermission, IsStaffPermission,)


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerPermission, IsStaffPermission,)
