from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model= Livro
        fields= ["titulo", "autor"]
        labels= {
            "titulo": "Título",
        }
        widgets= {
            "titulo": forms.TextInput(attrs={"class": "input w-full"}),
            "autor": forms.Select(attrs={"class": "select w-full"}),
        }

