from django.conf.urls import  url

from . import  views


urlpatterns =[
    url(r'^(?P<code_id>\w+)$',views.activate),
    #url(r'^$',views.activate,name='activate'),
    #url(r'register/', views.register, name='register'),

]