from rest_framework import serializers
from .. import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        # [
        #     'id', 'user_name', 'student_id',
        #     'qq', 'class_belong', 'gender',
        #     'profile', 'first_will', 'second_will', 'department'
        # ]
        depth = 1
