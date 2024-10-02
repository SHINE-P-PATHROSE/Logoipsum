# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),  # Assuming this is your login page
    path('books/', views.book_list, name='book_list'),  # Make sure this path exists
    path('books/add/', views.add_book, name='add_book'),  # Path for adding a book
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Path for editing a book
    path('register/', views.register, name='register'),  # Path for registration
    path('logout/', views.logout, name='logout'),  # Path for logout
    path('authors/add/', views.add_author, name='add_author'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/edit/<int:author_id>/', views.edit_author, name='edit_author'),
    path('authors/<int:author_id>/', views.author_details, name='author_details'),


    path('update_book_status/<int:book_id>/', views.update_book_status, name='update_book_status'),
]





