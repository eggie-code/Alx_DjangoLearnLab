from rest_framework import serializers
from .models import Author, Books
from datetime import datetime

# serializer for book model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['id', 'title', 'publication_year', 'author']

    # custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in future.")
        return value
    # serializer for author model

    class AuthorSerializer(serializers.ModelSerializer):
        # nested serializer include books to Author
        books = BookSerializer(many=True, read_only=True)

        class Meta:
            model = Author
            field = ['id', 'name', 'books']
