from django.shortcuts import render,render_to_response
from .models import tag

from article.models import article
# Create your views here.

def getArticle_tag(request,tagName):
    Tag = tag.objects.get(name=tagName)
    articles = article.objects.filter(tag=Tag)
    return render_to_response("tag/tagArticles.html",{"articles":articles})