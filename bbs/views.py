from django.http import HttpResponse
from django.shortcuts import  render,redirect
from bbs.models import  Block
from django.contrib.auth.models import  User
import  uuid
import  os
from django.core.mail import  send_mail
from activate.models import  ActivationCode
from django.utils.timezone import  datetime,timedelta
from  message.models import  Message
from usercenter.models import  UserProfile
from django.contrib.auth.decorators import  login_required

import  logging

LOGGER = logging.getLogger('forum')


def index(request):
    # block_infos=[{'name':'运维专区','desc':'运维学习讨论区','manager':'admin'},
    #              {'name':'django专区','desc':'Django学习讨论区','manager':'admin'},
    #              {'name':'部落建设','desc':'有关部落建设的事宜','manager':'admin'}
    #              ]
    #block_infos =Block.objects.all().order_by("-id")
    LOGGER.info("start application")
    LOGGER.error("fail to start application")
    try:
        name = request.GET['name']
    except Exception as e:
        LOGGER.exception(e)
    block_infos = Block.objects.filter(status=0).order_by("-id")
    user_count=User.objects.filter(username=request.user,)
    #if len(user_count) != 0:
    if user_count :
        msg_cnt = Message.objects.filter(status=1, owner=request.user).count()
        return render(request, 'bbs/index.html', {'blocks': block_infos, 'msg_cnt': msg_cnt})
    else:
        return  render(request,'bbs/index.html',{'blocks':block_infos})


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if not username or not email:
            return render(request,"bbs/register.html",{"error":"用户名和邮箱都不能为空。","username":username,"email":email})
        if password != confirm:
            return render(request, 'bbs/register.html',
                          {'error': '再次输入的密码一致', 'password': password, 'confirm': confirm})

        userdata = User(username=username,email=email,password=password,is_active=False)
        userdata.save()
        #return HttpResponse('success register')
        #return  redirect('http://127.0.0.1:8000/activate')
        new_code = str(uuid.uuid4()).replace("-","")
        activate_link = 'http://127.0.0.1:8000/activate/%s' %(new_code)
        send_mail(subject='[Python部落论坛]激活邮件',
                        message="点击链接激活: %s " % activate_link,
                        # html_message=activate_email,
                        from_email='304749970@qq.com',
                        recipient_list=[email],
                        fail_silently=False)
        new_user=User.objects.get(username=username)
        activate_user=ActivationCode(username=new_user,activationcode=new_code,expire_time=datetime.now()+timedelta(1))
        activate_user.save()
        #return  redirect('http://%s/activate/%s' %(request.get_host(),new_code))
        return  render(request,'activate/activate.html')


        #if len(title) > 100 or len(content) > 10000:
        #    return render(request,"article/article_create.html",{"b":block,"error":"标题或内容太长了。","title":title,"content":content})

        # article = Article(block=block,title=title,content=content,status=0)
        # article.save()
        #return render(request,'article/article_create.html', {'b':block})



        #user = User(USERNAME=username,)
        #return  redirect("/article/list/%s" % block_id)
    return  render(request,'bbs/register.html')

# def sendmail(request):
#     activate_link = 'http://127.0.0.1:8000/activate'
#     res=send_mail(subject='[Python部落论坛]激活邮件',
#               message="点击链接激活: %s " % activate_link,
#               # html_message=activate_email,
#               from_email='304749970@qq.com',
#               recipient_list=['damon@hudongpai.com'],
#               fail_silently=False)



