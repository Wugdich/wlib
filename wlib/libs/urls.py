from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login-page', views.loginPage, name='login-page'),
    path('logout-page', views.logoutPage, name='logout-page'),
    path('register-page', views.registerPage, name='register-page'),

    path('libs', views.libs, name='libs'),
    path('book-lib/add-book/', views.addBook, name='add-book'),
    path('book-lib/<str:username>/', views.book_lib, name='book-lib'),
    path('book-lib/update-book/<str:pk>/', views.updateBook, name='update-book'),
    path('book-lib/delete-book/<str:pk>/', views.deleteBook, name='delete-book'),
]
