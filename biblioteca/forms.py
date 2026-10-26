from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model= Livro
        fields= ["titulo", "autor", "preco"]
        labels= {
            "titulo": "Título",
            "preco": "Preço",
        }
        widgets= {
            "titulo": forms.TextInput(attrs={"class": "input w-full"}),
            "autor": forms.Select(attrs={"class": "select w-full"}),
            "preco": forms.NumberInput(attrs={"class": "input w-full"}),
        }

