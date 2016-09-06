from django.conf.urls import url

from . import views

urlpatterns =[
    #url(r'^$',views.index,name='index'),
    url(r'create', views.comment, name='comment'),
    #url(r'create/(?P<aid>\d+)$', views.comment, name='comment'),

]