from .models import Author, Book
from datetime import datetime
from .models import Author, Books
from rest_framework import serializers
<< << << < HEAD

# serializer for book model
== == == =

# Serializer for the Book model
>>>>>> > a76a393f48dcf33a3301605469b390a4bbee3ed3


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['id', 'title', 'publication_year', 'author']

    # custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
<< << << < HEAD
                "Publication year cannot be in future.")
        return value
    # serializer for author model

    class AuthorSerializer(serializers.ModelSerializer):
        # nested serializer include books to Author
        books = BookSerializer(many=True, read_only=True)

        class Meta:
            model = Author
            field = ['id', 'name', 'books']


== == == =
                "Publication year cannot be in the future.")
        return value

# Serializer for the Author model


class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
>>>>>>> a76a393f48dcf33a3301605469b390a4bbee3ed3
