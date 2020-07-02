from django.urls import path
from . import views

urlpatterns = [
    path('enroll', views.UserInfo.as_view()),
    path('department', views.DepartmentInfo.as_view()),
    path('image/<str:name>', views.DepartmentBgImage.as_view()),
]
