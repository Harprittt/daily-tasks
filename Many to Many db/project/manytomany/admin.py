from django.contrib import admin
from .models import Book

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'book_description', 'publish_date', 'price', 'written_by']
