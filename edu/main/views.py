from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    return render(
        request,
        '_index.html',
    )
