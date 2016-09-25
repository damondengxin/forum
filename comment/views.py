from django.shortcuts import render,HttpResponse
from .models import  Comment
from article.models import  Article
from django.contrib.auth.admin import User
import  json
from message.models import  Message

# Create your views here.


def comment(request):
    if request.method == 'POST':
        username = request.POST['owner']
        ownerid= User.objects.get(username=username)
        article = request.POST['article_id']
        articleid=Article.objects.get(id=article)
        content = request.POST['content']
        to_comment_id = int(request.POST.get("to_comment_id", 0))
        #to_comment_id = int(request.POST['to_comment_id'])
        if to_comment_id != 0:
            to_comment = Comment.objects.get(id=to_comment_id)
            #owner=Comment.objects.get(to_comment_id=to_comment_id)
            #userowner=User.objects.get(username=owner)
            message_objs = Message(owner=to_comment.owner,content=to_comment,link=articleid,status=1)
            message_objs.save()

        else:
            to_comment = None
        comment_objs = Comment(owner=ownerid,article=articleid,content=content,status=0,to_comment=to_comment)
        data = {'status': 'ok','msg':'保存评论失败'}

        comment_objs.save()
        #comment_py = Comment.objects.get(article=article)
        data=json.dumps(data)
        return  HttpResponse(data)


        #return HttpResponse(ownerid,articleid,content)

    #return  render(request,'comment/create_comment.html')
    #return  HttpResponse('test')