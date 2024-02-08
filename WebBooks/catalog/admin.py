from django.contrib import admin
from catalog.models import *


@admin.register(Author)
class AuthotAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )



admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
