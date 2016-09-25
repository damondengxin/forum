from django.conf.urls import  url

from . import views

urlpatterns =[
    url(r'list',views.message,name='message'),
    url(r'read',views.read,name='read'),

]