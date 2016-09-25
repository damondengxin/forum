from django.shortcuts import render,HttpResponse
from message.models import  Message
from django.contrib.auth.models import User
from comment.models import Comment
from article.models import  Article
import  json


# Create your views here.


def message(request):
    if request.user:
        user= User.objects.get(username=request.user)
        unread=Message.objects.filter(owner=user.id,status=1).order_by("-id")
        return render(request,"message/message.html",{'unread':unread})


def read(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        contentid = request.POST['contentid']
        #linkid = request.POST['linkid']
        #content_objs= Comment.objects.get(id=contentid)
        #Article_objs = Article.objects.get(content=linkid)
        message_objs = Message.objects.filter(owner=user,content_id=contentid)
        for mess in message_objs:
            mess.status=0
            mess.save()

        #to_comment_id = int(request.POST.get("to_comment_id", 0))
        # if to_comment_id != 0:
        #     to_comment = Comment.objects.get(id=to_comment_id)
        #     # owner=Comment.objects.get(to_comment_id=to_comment_id)
        #     # userowner=User.objects.get(username=owner)
        #     message_objs = Message(owner=to_comment.owner, content=to_comment, link=articleid, status=1)
        #     message_objs.save()
        #
        # else:
        #     to_comment = None
        # comment_objs = Comment(owner=ownerid, article=articleid, content=content, status=0, to_comment=to_comment)
        data = {'status': 'ok', 'msg': '修改messag数据失败'}

        # comment_py = Comment.objects.get(article=article)
        data = json.dumps(data)
        return HttpResponse(data)
