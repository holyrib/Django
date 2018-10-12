from django.db import models
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    owner = models.CharField(max_length=100)

class Comment(models.Model):
    owner = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
