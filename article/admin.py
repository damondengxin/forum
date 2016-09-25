from django.contrib import admin

# Register your models here.

from . models import  Article
from comment.models import  Comment


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete =  False

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block","title","status","create_timestamp","last_update_timestamp")
    actions = ['make_picked']
    search_fields = ['title']
    inlines = [CommentInline]
    def make_picked(modeadmin,request,queryset):
        for a in queryset:
            a.status =10
            a.save()
    make_picked.short_description = "设置精华"




admin.site.register(Article,ArticleAdmin)