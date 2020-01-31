from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    post_type = models.CharField(max_length=10)
    brief = models.TextField()
    text = models.TextField()
    url = models.CharField(max_length=20)
    date = models.DateTimeField(timezone.now())
    like = models.IntegerField(default=0)
    cover = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Comment(models.Model):
    nickname = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nickname