from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('book-lib', views.book_lib, name='book-lib'),
    path('game-lib', views.game_lib, name='game-lib'),
    path('movie-lib', views.movie_lib, name='movie-lib'),
    path('book-lib/add-book/', views.addBook, name='add-book'),
]
