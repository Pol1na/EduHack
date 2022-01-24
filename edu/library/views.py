from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect
from .models import Book, Author, Genre
# from .forms import BookForm



class HomeBook(ListView):
    model = Book
    context_object_name = 'books'
    #paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Библиотека'
        return context

    def get_queryset(self):
        return Book.objects.all()
