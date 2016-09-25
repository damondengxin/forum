from django.conf.urls import  url

from . import views

urlpatterns =[
    url(r'uploadavatar',views.upload_avatar,name='upload_avatar'),

]