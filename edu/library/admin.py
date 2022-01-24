from django.contrib import admin
from .models import Book, Genre, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'download_amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_display_links = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name', 'surname', 'patronymic',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
