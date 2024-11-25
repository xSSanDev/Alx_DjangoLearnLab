# api/models.py

from django.db import models

class Author(models.Model):
    """
    The Author model represents an author with a name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a book with a title, publication year, and a foreign key to the Author model.
    The foreign key establishes a one-to-many relationship from Author to Books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title