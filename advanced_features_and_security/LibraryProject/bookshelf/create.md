```python
from bookshelf.models import Book

# Create a new Book instance using the create method
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

# Expected output: Book instance with title '1984', author 'George Orwell', and publication year 1949 created successfully.