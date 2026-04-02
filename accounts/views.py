from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView
)
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
