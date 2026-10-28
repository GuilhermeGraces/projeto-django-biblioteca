from django.urls import path

from biblioteca.views import InspecionarView, catalogo, deletar, editar, home, livros

urlpatterns = [
    path("", home, name="home"),
    path("livros/", livros, name="livros"),
    path("livros/<int:pk>/deletar/", deletar, name="deletar"),
    path("livros/<int:pk>/editar/", editar, name="editar"),
    path("catalogo/", catalogo, name="catalogo"),
    path("catalogo/<int:pk>/", InspecionarView.as_view(), name="inspecionar"),
]