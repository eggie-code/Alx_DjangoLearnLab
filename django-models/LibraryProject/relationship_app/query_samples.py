from relationship_app.models import Author, Book, Library, Librarian
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


author_name = "George Orwell"
author = Author.objects.create(name=author_name).first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f" - {book.title}")
else:
    print(f"No author found with the name {author_name}.")

library_name = "Central Library"
library = Library.objects.filter(name=library_name).first()
if library:
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f" - {book.title}")
else:
    print(f"No library found with the name {library_name}.")


if library:
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library.name}.")
