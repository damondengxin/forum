from django.conf.urls import  url

from .views import  article_list
#from .views import  article_create
from .views import  ArticleCreateView
from .views import article_detail
#from .views import  ArticleDetailView
from django.contrib.auth.decorators import  login_required


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)',article_list),
    #url(r'^create/(?P<block_id>\d+)',article_create),
    url(r'^create/(?P<block_id>\d+)',login_required(ArticleCreateView.as_view())),
    url(r'^detail/(?P<aid>\d+)', article_detail),
    #url(r'^detail/(?P<pk>\d+)', ArticleDetailView.as_view()),

]