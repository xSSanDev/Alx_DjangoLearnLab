```python
from bookshelf.models import Book

# Retrieve the Book instance with the title '1984'
book = Book.objects.get(title='1984')

# Update the title
book.title = 'Nineteen Eighty-Four'

# Save the changes to the database
book.save()

# Expected output: Book instance with title 'Nineteen Eighty-Four' updated successfully.