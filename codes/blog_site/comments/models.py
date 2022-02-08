from django.db import models
from blogs.models import BlogPost
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    objects = models.Manager()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text