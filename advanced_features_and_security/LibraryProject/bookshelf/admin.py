from django.contrib import admin
from .models import Book  # import book model

# custom admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    search_fields = ('title', 'author')

    list_filter = ('publication_year',)


# register the book model
admin.site.register(Book, BookAdmin)
# Register your models here.
