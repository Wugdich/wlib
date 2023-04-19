from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

from . import forms
from . import models


def home(request):
    context = {
            }
    return render(request, 'home.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
                request,
                username=username,
                password=password,
                )
        if user:
            login(request, user)
            return redirect('libs')
        else:
            messages.error(request, "Wrong username or password") 
    context = {
            }
    return render(request, 'libs/login_page.html', context)

def libs(request):
    context = {
            }
    return render(request, 'libs/libs.html', context)

def book_lib(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    query = (
            Q(title__icontains=q) |
            Q(author__icontains=q) |
            Q(publish_year__icontains=q) |
            Q(status__icontains=q)  # TODO: not correct search for status field
            )
    books = models.Book.objects.filter(query)
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
        return redirect('book-lib')

    context = {
            'form': form, 
            }
    return render(request, 'libs/book_form.html', context)

def updateBook(request, pk):
    book = models.Book.objects.get(id=pk)
    form = forms.BookForm(instance=book)

    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('book-lib')

    context = {
            'form': form,
            'book': book,
            }
    return render(request, 'libs/book_form.html', context)

def deleteBook(request, pk):
    book = models.Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-lib')

    context = {
            "obj": book,
            }
    return render(request, 'delete.html', context)

def game_lib(request):
    context = {
            }
    return render(request, 'libs/game_lib.html', context)

def movie_lib(request):
    context = {
            }
    return render(request, 'libs/movie_lib.html', context)
