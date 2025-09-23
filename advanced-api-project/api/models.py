from django.db import models

# Author model stores author information


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model stores book information and links to Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship from Author to Books
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
