# api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

class BookListView(generics.ListAPIView):
    """
    View to list all books in the system.
    Allows unauthenticated users to access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID.
    Allows unauthenticated users to access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic before saving the instance
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic before updating the instance
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]