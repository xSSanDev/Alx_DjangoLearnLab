# CRUD Operations in Django Shell

## Create
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book(title='1984', author='George Orwell', publication_date=1949)

# Save the instance to the database
book.save()

# Expected output: Book instance with title '1984', author 'George Orwell', and publication year 1949 created successfully.