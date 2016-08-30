from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import  send_mail
import  uuid
from .models import  ActivationCode
from django.contrib.auth.admin import  User
from django.utils import  timezone

# Create your views here.

# active_link='test'
# active_email =''' 点击 <a href="%s"> 这里</a>激活''' % active_link
# send_mail("")

def activate(request,code_id):
    #activationcode=str(uuid.uuid4()).replace("-","")
    #return HttpResponse("test")
    #code_id = int(code_id)

    activate_objs = ActivationCode.objects.get(activationcode=code_id)
    name = activate_objs.username
    User_objs = User.objects.get(username=name)
    if activate_objs.activationcode == code_id:
        if timezone.now() < activate_objs.expire_time:
            #return render(request,'activate/activate.html')
            User_objs.is_active=True
            User_objs.save()
            return  redirect(request,'registration/login.html')
