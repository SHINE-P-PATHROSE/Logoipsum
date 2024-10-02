from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'create_date', 'action', 'status')
    search_fields = ('book_name', 'author_name')  # Corrected search fields
    list_filter = ('status', 'author_name')
    ordering = ('-create_date',)

admin.site.register(Book, BookAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'action_status')
    search_fields = ('name', 'username', 'email')
