from django.db import models
from django.contrib.auth.models import User
from comment.models import Comment
from article.models import Article

# Create your models here.

class Message(models.Model):
    owner = models.ForeignKey(User,verbose_name='作者')
    content = models.ForeignKey(Comment,verbose_name='被评论的内容')
    link = models.ForeignKey(Article,verbose_name='评论的链接')
    status = models.IntegerField('状态',choices=(('0','已读'),('1','未读')))

    # def __str__(self):
    #     return  self.status