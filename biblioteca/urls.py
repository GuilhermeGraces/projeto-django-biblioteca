from django.urls import path

from biblioteca.views import deletar, editar, home, livros

urlpatterns = [
    path("", home, name="home"),
    path("livros/", livros, name="livros"),
    path("livros/<int:pk>/deletar/", deletar, name="deletar"),
    path("livros/<int:pk>/editar/", editar, name="editar"),
]