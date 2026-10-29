from django.db import models

# Create your models here.
class Autor(models.Model):
    nome= models.CharField(max_length=100)
    sobrenome= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Genero(models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    genero= models.ForeignKey(Genero, on_delete=models.PROTECT, null=True, blank=True)
    capa= models.ImageField(upload_to="capas/", blank=True)
    
    def __str__(self):
        return f"{self.titulo}"

class Cartaz(models.Model):

    OPCOES=[
        ("recomendo","Recomendo"),
        ("nao_recomendo","Não recomendo"),
        ("neutro","Neutro"),
    ]

    livro= models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    texto = models.TextField(max_length=500)
    avaliacao = models.CharField(max_length=15, choices=OPCOES, default="neutro")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} sobre {self.livro}"

    class Meta:
        ordering = ["-data"]