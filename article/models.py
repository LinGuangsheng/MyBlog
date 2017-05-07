#coding=utf-8
from django.db import models
from markdown import markdown
from slugify import slugify
from category.models import category
from tag.models import tag
import pinyin
# Create your models here.

class article(models.Model):

    # 博文标题
    title = models.CharField(max_length=40)
    # 博文的slug
    slug = models.SlugField(blank=True,null=True)

    # 博文的内容主体
    body = models.TextField()

    markdownBody = models.TextField(blank=True,null=True)

    # 博文的创建时间
    created = models.DateTimeField(auto_now_add=True)
    # 博文的更新时间
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(category,blank=True,null=True)

    tag = models.ManyToManyField(tag)

    def ready(self):
        self.slug = slugify(pinyin.get(self.title,delimiter='-'))
        self.markdownBody = markdown(self.body)

    def save(self,*args,**kwargs):
        self.ready()
        super(article,self).save(*args,**kwargs)



