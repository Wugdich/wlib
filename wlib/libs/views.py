from django.shortcuts import redirect, render

from . import forms
from . import models

# Create your views here.

def home(request):
    context = {
            }
    return render(request, 'libs/home.html', context)

def book_lib(request):
    books = models.Book.objects.all()
    context = {
            'books': books,
            }
    return render(request, 'libs/book_lib.html', context)

def addBook(request):
    form = forms.BookForm()
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
            'form': form, 
            }
    return render(request, 'libs/book_form.html', context)

def game_lib(request):
    context = {
            }
    return render(request, 'libs/game_lib.html', context)

def movie_lib(request):
    context = {
            }
    return render(request, 'libs/movie_lib.html', context)
