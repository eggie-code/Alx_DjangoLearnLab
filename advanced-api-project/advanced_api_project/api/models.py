from django.db import models

# Author model to store author info


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model stores book info
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    # foreignkey one to many relationship from author to Books.
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        returnself.title
