from django.urls import path

from biblioteca.views import deletar, home, livros

urlpatterns = [
    path("", home, name="home"),
    path("livros/", livros, name="livros"),
    path("livros/<int:pk>/deletar/", deletar, name="deletar")
]