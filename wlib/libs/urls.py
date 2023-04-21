from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login', views.loginPage, name='login-page'),
    path('logout', views.logoutPage, name='logout-page'),
    path('register', views.registerPage, name='register-page'),

    path('libs', views.libs, name='libs'),
    path('lib/add-book/', views.addBook, name='add-book'),
    path('lib/<str:username>/', views.lib, name='lib'),
    path(
        'book-lib/<str:username>/profile/', 
        views.profilePage, 
        name='profilePage'
        ),
    path('book-lib/update-book/<str:pk>/', views.updateBook, name='update-book'),
    path('book-lib/delete-book/<str:pk>/', views.deleteBook, name='delete-book'),
]
