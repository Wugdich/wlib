from django.shortcuts import render

# Create your views here.

def home(requests):
    context = {
            }
    return render(requests, 'libs/home.html', context)

def book_lib(requests):
    context = {
            }
    return render(requests, 'libs/book_lib.html', context)
