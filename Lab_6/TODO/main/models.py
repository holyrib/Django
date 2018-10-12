from django.db import models
import datetime
# Create your models here.
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    due = models.DateTimeField()
    owner = models.CharField(max_length=100)
    status = models.BooleanField(default=False)