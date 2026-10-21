from django.urls import path

from biblioteca.views import home, livros

urlpatterns = [
    path("", home, name="home"),
    path("livros/", livros, name="livros")
]