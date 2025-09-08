from django.db import models
from django.utils import timezone
from django.contrib.auth import AbstractUser, BaseuserManager


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(usernams=username, email=email, **extrafields)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra fields):
        extra_fields.stedefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
