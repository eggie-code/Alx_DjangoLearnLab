from django.db import models

<<<<<<< HEAD
# Author model to store author info
=======
# Author model stores author information
>>>>>>> a76a393f48dcf33a3301605469b390a4bbee3ed3


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

<<<<<<< HEAD

# Book model stores book info
=======
# Book model stores book information and links to Author


>>>>>>> a76a393f48dcf33a3301605469b390a4bbee3ed3
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

<<<<<<< HEAD
    # foreignkey one to many relationship from author to Books.
=======
    # ForeignKey creates a one-to-many relationship from Author to Books
>>>>>>> a76a393f48dcf33a3301605469b390a4bbee3ed3
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
<<<<<<< HEAD
        returnself.title
=======
        return self.title
>>>>>>> a76a393f48dcf33a3301605469b390a4bbee3ed3
