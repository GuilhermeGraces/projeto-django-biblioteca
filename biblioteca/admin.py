from django.contrib import admin
from .models import Autor, Cartaz, Genero, Livro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Livro)
admin.site.register(Cartaz)
