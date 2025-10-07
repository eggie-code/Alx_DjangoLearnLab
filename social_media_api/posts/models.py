from django.db import models
from django.conf import settings
from django.apps import apps
from rest_framework import viewsets


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ensures a user can like a post only once
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


def some_method(self):
    Like = apps.get_model('posts', 'Like')


def get_post_model():
    Post = apps.get_model('posts', 'Post')
    return Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = get_post_model().objects.all().order_by('-created_at')
