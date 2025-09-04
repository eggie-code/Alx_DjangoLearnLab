from relationship_app.models import Author, Book, Library, Librarian
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()


author = Author.objects.get(name="J.K Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(f"- {book.title}")


library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library.name}:")
for book in books_in_library:
    print(f"- {book.title} by {book.author.name}")


librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian: {librarian.name}: {librarian.name}")
