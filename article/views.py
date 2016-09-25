from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
# Create your views here.
from  article.models import  Article
from bbs.models import  Block
from article.forms import  ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.admin import  User
from comment.models import Comment
from message.models import Message


def paginate_queryset(objs,page_no,cnt_per_page=2,half_show_length=5):
    p = Paginator(objs,cnt_per_page)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no <= 0:
        page_no =1
    page_links = [ i for i in range(page_no - half_show_length,page_no + half_show_length +1 )
                   if i>0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0] -1
    next_link = page_links[-1] +1
    pagination_data = {
        "has_previous": previous_link >0,
        "has_next" :next_link <= p.num_pages,
        "previous_link":previous_link,
        "next_link":next_link,
        "page_cnt":p.num_pages,
        "current_no":page_no,
        "page_links":page_links
    }
    return (page.object_list,pagination_data)



# def article_list(request,block_id):
#     block_id = int(block_id)
#     block = Block.objects.get(id=block_id)
#     #articles_objs = Article.objects.filter(block__id=block_id,status=0).order_by("-id")
#     ARTICLE_CNT_1PAGE=1
#     page_no = int(request.GET.get('page_no',"1"))
#     # start_index=(page_no -1) * ARTICLE_CNT_1PAGE
#     # end_index = page_no * ARTICLE_CNT_1PAGE
#     #articles_objs = Article.objects.filter(block=block,status=0).order_by("-id")[start_index:end_index]
#     all_articles = Article.objects.filter(block__id=block_id,status=0).order_by("-id")
#     p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
#     #总页数
#     page_cnt = p.num_pages
#     #当前页码
#     current_no = page_no
#
#     #标页列表
#     page_links = [ i for i  in range(page_no -5,page_no + 6) if i > 0 and i <= p.num_pages]
#     #最小页-1
#     previous_link = page_links[0] -1
#     #最大页
#     next_link = page_links[-1] +1
#     #有前页
#     has_previous = previous_link >0
#     #有后页
#     has_next = next_link <= page_cnt
#
#
#
#     page = p.page(page_no)
#     articles_objs = page.object_list
#
#     return render(request, 'article/article_list.html',{'articles':articles_objs,'current':current_no,'page_cnt':page_cnt,
#                                                         'b':block,'pan':page_no,'plinks':page_links,'plink':previous_link,'nlink':next_link,
#                     'has_previous':has_previous,'has_next':has_next})


##v2
def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block = block, status=0).order_by("-id")
    page_articltes,pagination_data = paginate_queryset(all_articles,page_no)
    return render(request,"article/article_list.html",{"articles":page_articltes,"b":block,
                                                       "pagination_data":pagination_data})





##用于检查用户有没有登录,如果检查到没有登录,则会重定向到LOGIN_URL,默认值是accounts/login
#@login_required()
# def article_create(request,block_id):
#     block_id = int(block_id)
#     block = Block.objects.get(id=block_id)
#     # v1 version
#     #if request.method == 'GET':
#         # articles_objs = Article.objects.filter(block__id=block_id,status=0).order_by("-id")
#         #articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
#     #   return render(request,'article/article_create.html', {'b':block})
#
#
#
#     # else:
#     #     title = request.POST["title"]
#     #     content = request.POST['content']
#     #     if not title or not content:
#     #         return render(request,"article/article_create.html",{"b":block,"error":"标题和内容都不能为空。","title":title,"content":content})
#     #     if len(title) > 100 or len(content) > 10000:
#     #         return render(request,"article/article_create.html",{"b":block,"error":"标题或内容太长了。","title":title,"content":content})
#     #     article = Article(block=block,title=title,content=content,status=0)
#     #     article.save()
#     #     #return render(request,'article/article_create.html', {'b':block})
#     #     return  redirect("/article/list/%s" % block_id)
#
#     #v2 version
#     # form=ArticleForm(request.POST)
#     # if form.is_valid():
#     #     article=Article(block=block,title=form.cleaned_data['title'],content=form.cleaned_data['content'],status=0)
#     #     article.save()
#     #     return  redirect("/article/list/%s" % block_id)
#     # else:
#     #     return  render(request,'article/article_create.html',{'b':block,"form":form})
#
    # #v3 version
    # form=ArticleForm(request.POST)
    # if form.is_valid():
    #     article=form.save(commit=False)
    #     article.block = block
    #     article.status =0
    #     article.save()
    #     return  redirect("/article/list/%s" % block_id)
    # else:
    #     return  render(request,'article/article_create.html',{'b':block,"form":form})


class ArticleCreateView(View):
    template_name = 'article/article_create.html'
    def init_data(self,block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)
        # self.username = username
        # self.user = User.objects.get(id= username)
    def get(self,request,block_id):
        self.init_data(block_id)

        return render(request,self.template_name,{'b':self.block})
    def post(self,request,block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)

        #username = request.user
        #userinfo = User.objects.get(username=username)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            #获取当前用户的request.user
            #article.owner = request.user
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % self.block_id)
        else:
            return  render(request,self.template_name,{'b':self.block,'form':form})


def article_detail(request,aid):
    article=Article.objects.get(id=aid)
    #comment_objs = Comment.objects.filter(article=aid)
    page_no = int(request.GET.get("page_no", "1"))
    comment_objs = Comment.objects.filter(article=aid, status=0).order_by("-id")
    page_comment, pagination_data = paginate_queryset(comment_objs, page_no)


    return render(request,'article/article_detail.html',{'article':article,'comment':page_comment,"pagination_data":pagination_data})


# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'article/article_detail.html'
#     context_object_name = 'a'
