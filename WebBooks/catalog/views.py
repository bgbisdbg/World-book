from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance, Author


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_availble = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_availble': num_instances_availble,
                           'num_authors': num_authors,

                           })
