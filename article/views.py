from django.shortcuts import render,render_to_response
from .models import article
# Create your views here.

def index(request):
    articles = article.objects.all()[:10]
    return render_to_response("blog/index.html",{'articles':articles})

def getArticle(request,slug):
    print("Here")
    print(slug)
    Article = article.objects.get(slug=slug)
    return render_to_response("article/article.html",{'article':Article})