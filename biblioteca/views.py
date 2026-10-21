from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Livro

# Create your views here.
def home(request):
    return render(request, "biblioteca/home.html")

def livros(request):
    lista_livros = Livro.objects.order_by("titulo")
    paginator = Paginator(lista_livros, 2)

    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)

    return render(request, "biblioteca/livros.html", {"page_obj": page_obj})