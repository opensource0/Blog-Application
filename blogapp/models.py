from django.db import models
from django.contrib.auth.models import User;
# Create your models here.

class BlogArticle(models.Model):
    title = models.CharField(max_length=400);
    text = models.TextField();
    author = models.ForeignKey(User,on_delete='User')

    # def __str__(self):
    #     list = [self.title,self.author,self.title]
    #     return list
