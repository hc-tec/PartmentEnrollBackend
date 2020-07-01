from django.db import models

class User(models.Model):
    GENDER = (
        (1, '男'),
        (2, '女')
    )
    WILL = (
        (1, '研发部'),
        (2, 'acm 部'),
        (3, '行政部'),
        (4, 'ctf 部')
    )
    USER_TYPE = (
        (1, 'student'),
        (2, 'charger'),
        (3, 'admin'),
    )
    user_name = models.CharField(max_length=16)
    student_id = models.CharField(max_length=10)
    avatar = models.CharField(max_length=128, null=True, blank=True)
    type = models.IntegerField(choices=USER_TYPE, default=1)
    qq = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER, default=1)
    first_will = models.IntegerField(choices=WILL, null=True, blank=True)
    second_will = models.IntegerField(choices=WILL, null=True, blank=True)

    def __str__(self):
        return self.user_name
