from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login-page', views.loginPage, name='login-page'),
    path('logout-page', views.logoutPage, name='logout-page'),

    path('libs', views.libs, name='libs'),

    path('game-lib', views.game_lib, name='game-lib'),
    path('movie-lib', views.movie_lib, name='movie-lib'),

    path('book-lib', views.book_lib, name='book-lib'),
    path('book-lib/add-book/', views.addBook, name='add-book'),
    path('book-lib/update-book/<str:pk>/', views.updateBook, name='update-book'),
    path('book-lib/delete-book/<str:pk>/', views.deleteBook, name='delete-book'),
]
