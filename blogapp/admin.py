from django.contrib import admin
from .models import BlogArticle

# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author']


admin.site.register(BlogArticle,BlogArticleAdmin)
