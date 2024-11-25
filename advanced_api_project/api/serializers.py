# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    The BookSerializer serializes all fields of the Book model.
    It includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    The AuthorSerializer serializes the name field of the Author model.
    It also includes a nested BookSerializer to serialize the related books dynamically.
    The relationship between Author and Book is handled using the related_name 'books' defined in the Book model.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']