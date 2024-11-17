```python
from bookshelf.models import Book

# Retrieve the Book instance with the title '1984'
book = Book.objects.get(title='1984')

# Display all attributes of the book
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_date}")

# Expected output: Title: 1984, Author: George Orwell, Publication Year: 1949