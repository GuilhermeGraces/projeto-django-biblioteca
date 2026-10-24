from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import HttpResponse

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


@require_POST
def deletar(request, pk):
    livro= get_object_or_404(Livro, pk=pk)
    livro.delete()
    return HttpResponse("")