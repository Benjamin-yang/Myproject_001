from django.urls import path

from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('addBook', views.addBook, name='addBook'),
    path('delBook/<int:book_id>', views.deleteBook, name='delBook'),
]
