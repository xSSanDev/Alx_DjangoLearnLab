```python
from bookshelf.models import Book

# Retrieve the Book instance with the title 'Nineteen Eighty-Four'
book = Book.objects.get(title='Nineteen Eighty-Four')

# Delete the instance
book.delete()

# Confirm the deletion by trying to retrieve all books
books = Book.objects.all()
print(books)

# Expected output: QuerySet containing all remaining Book instances, confirming the deletion of 'Nineteen Eighty-Four'.