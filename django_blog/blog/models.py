from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model


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

    def __str__(self):
        # This makes the object easily readable in the Django Admin
        return self.title
