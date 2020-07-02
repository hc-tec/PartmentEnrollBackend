

from rest_framework.views import APIView
from rest_framework.viewsets import generics
from .utils import serializer
from . import models

from django.http import JsonResponse

class UserInfo(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserInfoSerializer




