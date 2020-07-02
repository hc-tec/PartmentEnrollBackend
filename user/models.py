from django.db import models

class User(models.Model):
    GENDER = (
        (1, '男'),
        (2, '女')
    )
    WILL = (
        (1, '研发部'),
        (2, 'acm 部'),
        (3, 'ctf 部')
    )
    user_name = models.CharField(max_length=16, unique=True, null=False, blank=False)
    student_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
    qq = models.CharField(max_length=10)
    class_belong = models.CharField(max_length=32, default='')
    gender = models.IntegerField(choices=GENDER, default=1)
    profile = models.TextField(default='')
    first_will = models.IntegerField(choices=WILL, default=1, null=False, blank=False)
    second_will = models.IntegerField(choices=WILL, default=1, null=False, blank=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.user_name

class Department(models.Model):
    name = models.CharField(max_length=8, default='', primary_key=True)
    profile = models.TextField()
    bgImage = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name


