from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from DLS import views
urlpatterns = [
    url('new-books',views.addBook),
    url(r'^add',views.add),
    url('view-books',views.ViewBooks),
    url('edit-books',views.edit_book),
    url('edit',views.edit),
    url('delete-books',views.delete),
    url('search-books',views.searchBook),
    url('search',views.search),
    url('login',views.userLogin),
    url('logout',views.userLogout),
]
