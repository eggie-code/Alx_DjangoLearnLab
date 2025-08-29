from django.db import models
from bookshelf.models import Book


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.IntegerField()

    def __str__(self):
        return self.title


book = Book.object.create(
    title="1984", author="George Orwell", publication_year=1949)

# Create your models here.
