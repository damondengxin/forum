from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.IntegerField("性别",choices=((0,'男'),(-1,'女')),
                              default=0)
    brithday = models.DateTimeField("生日",null=True,blank=True)
    avatar = models.CharField("头像",max_length=300,blank=True)

    def __str__(self):
        return  self.avatar