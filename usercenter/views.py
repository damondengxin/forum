from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
import os

# Create your views here.

@login_required
def upload_avatar(request):
    if request.method == "GET":
        return render(request,'usercenter/upload_avatar.html')
    else:
        profile = request.user.userprofile
        avatar_file = request.FILES.get('avatar',None)
    file_path = os.path.join("/data/project/forum/userres/avatar/",avatar_file.name)
    with open(file_path,"wb+") as destination:
        for chunk in avatar_file.chunks():
            destination.write(chunk)
    url = "http://res.myforum.com/media/avatar/%s" %avatar_file.name
    profile.avatar = url
    profile.save()
    return  redirect("/bbs")
