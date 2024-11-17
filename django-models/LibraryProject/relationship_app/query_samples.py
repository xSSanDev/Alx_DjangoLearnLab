import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

if __name__ == "__main__":
    # Example usage
    author_name = "Author Name"
    library_name = "Library Name"

    books_by_author = query_books_by_author(author_name)
    if books_by_author:
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(book.title)
    else:
        print(f"No books found for author: {author_name}")

    books_in_library = list_books_in_library(library_name)
    if books_in_library:
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(book.title)
    else:
        print(f"No books found in library: {library_name}")

    librarian = retrieve_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
    else:
        print(f"No librarian found for library: {library_name}")