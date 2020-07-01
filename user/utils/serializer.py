from rest_framework import serializers
from .. import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        depth = 1
