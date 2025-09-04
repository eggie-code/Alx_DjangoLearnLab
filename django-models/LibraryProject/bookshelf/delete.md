```python
from bookshelf.models import Book
#delete
book.delete()

try:
    book=Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:    

    print("Book not found.")