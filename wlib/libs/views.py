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

def game_lib(requests):
    context = {
            }
    return render(requests, 'libs/game_lib.html', context)

def movie_lib(requests):
    context = {
            }
    return render(requests, 'libs/movie_lib.html', context)
