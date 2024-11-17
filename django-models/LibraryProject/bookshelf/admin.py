from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
    ordering = ('-publication_year',)
    fields = ('title', 'author', 'publication_year')
    favorite_books = Book.objects.filter(title__icontains='Python')

admin.site.register(Book, BookAdmin)