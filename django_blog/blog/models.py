from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_lenght=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def__str__(self):
        return self.title
