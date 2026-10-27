from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import LivroForm

from .models import Genero, Livro

# Create your views here.
def home(request):
    return render(request, "biblioteca/home.html")

def livros(request):
    if not request.user.is_staff:
        return redirect("home")
    lista_livros = Livro.objects.order_by("titulo")
    paginator = Paginator(lista_livros, 2)

    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)

    return render(request, "biblioteca/livros.html", {"page_obj": page_obj})


@require_POST
def deletar(request, pk):
    if not request.user.is_staff:
            return redirect("home")
    livro= get_object_or_404(Livro, pk=pk)
    livro.delete()
    return HttpResponse("")

def editar(request, pk):
    if not request.user.is_staff:
            return redirect("home")
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form= LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return render(request, "biblioteca/partials/livro.html", {"livro":livro})
    else:
        form= LivroForm(instance=livro)
    return render(request, "biblioteca/partials/livro_form.html", {"form": form, "livro":livro})


def catalogo(request):
    generos = Genero.objects.order_by("nome")
    return render(request, "biblioteca/catalogo.html", {"generos":generos})

    
