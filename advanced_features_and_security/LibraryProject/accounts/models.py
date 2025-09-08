from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    class CustomerUser(AbstractUser):
        username = None
        email = models.EmailField(unique=True)
        date_of_birth = models.DateField(null=True, blank=True)
        profile_photo = models.ImageField(
            upload_to='profile_photos/', null=True, blank=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']
        objects = BaseUserManager()

        def __str__(self):
            return self.username
