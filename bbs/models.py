from django.db import models

# Create your models here.

class Block(models.Model):
    name=  models.CharField('板块名称',max_length=100)
    desc= models.CharField('板块描述',max_length=100)
    manager_name = models.CharField('板块管理名称',max_length=100)

