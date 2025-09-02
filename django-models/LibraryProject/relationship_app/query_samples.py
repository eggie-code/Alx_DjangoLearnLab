from relationship_app.models import author, Book, Library, Librarian
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()


def run_queries():
    authors_name = "Author Name"
    try:
        author = Author.objects.get(name=authors_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {authors_name}:")
        for book in books_by_author:
            print(f"Book Title: {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{authors_name}' does not exist.")

    library_name = "Library Name"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(f"Book Title: {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")


if __name__ == "__main__":
    run_queries()
