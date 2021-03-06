"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import  django
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import  views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bbs/',include('bbs.urls')),
    url(r'^article/',include('article.urls')),
    url(r'^activate/', include('activate.urls')),
    url(r'^comment/',include('comment.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')) ,
    url(r'^password_reset/$',auth_views.password_reset,name='password_reset'),
    #url(^password_reset/$ [name='password_reset']),
    url(r'^password_reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset/done/$',auth_views.password_reset_complete,name='password_reset_complete'),
    url(r'^password_change/$',auth_views.password_change,name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^message/',include('message.urls')),
    url(r'^usercenter/',include('usercenter.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]

admin.site.disable_action('delete_selected')
