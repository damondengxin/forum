from django import  forms
from .models import Article

#v1 version
# class ArticleForm(forms.Form):
#     title = forms.CharField(label="标题",max_length=100)
#     content = forms.CharField(label="内容",max_length=10000)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']