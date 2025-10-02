from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """
    Model for a single blog post entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Stores the date and time the post was created (automatically set on creation)
    published_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey creates a one-to-many relationship: One User can write many Posts.
    # on_delete=models.CASCADE means if the User is deleted, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        # This makes the object easily readable in the Django Admin
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Comment(models.Model):
    # 'related_name' allows us to fetch comments using post.comments.all()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Order comments by creat time, oldest first
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
