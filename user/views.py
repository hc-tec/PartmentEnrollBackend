

from rest_framework.views import APIView
from rest_framework.viewsets import generics
from .utils import serializer
from . import models

from django.http import JsonResponse

class UserRegister(generics.CreateAPIView):
    queryset = models.User
    serializer_class = serializer.UserInfoSerializer
