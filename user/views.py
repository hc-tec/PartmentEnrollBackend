

from rest_framework.views import APIView
from rest_framework.viewsets import generics
from .utils import serializer
from . import models

from django.http import JsonResponse

class UserInfo(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserInfoSerializer

class DepartmentInfo(generics.ListAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializer.DepartmentInfoSerializer

class DepartmentBgImage(APIView):
    def patch(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '保存成功'}
        name = kwargs['name']
        image = request.data['image']
        print(image)
        Department =  models.Department.objects.filter(name=name)
        if Department:
            Department.__dict__['bgImage'] = image
            Department.save()
        else:
            ret['code'] = 400
            ret['msg'] = '此部门不存在'
        return JsonResponse(ret)

