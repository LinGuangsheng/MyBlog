from django.contrib import admin
from .models import *


# Register your models here.

class articleAdmin(admin.ModelAdmin):
    fields = ['title','body','markdownBody','category','tag']

admin.site.register(article,articleAdmin)
