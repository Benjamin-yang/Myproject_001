from django.urls import path

from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('addBook', views.addBook, name='addBook'),

]
