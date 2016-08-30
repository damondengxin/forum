from django.db import models
from django.contrib.auth.admin import  User
from django.utils.timezone import  datetime,timedelta

# Create your models here.


class ActivationCode(models.Model):
    username = models.ForeignKey(User,verbose_name="用户名")
    activationcode = models.CharField('激活码',max_length=50)
    expire_time = models.DateTimeField('过期时间')

    # def __str__(self):
    #     return  self.username