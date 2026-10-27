from django.db import models

# Create your models here.
class Autor(models.Model):
    nome= models.CharField(max_length=100)
    sobrenome= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.titulo}"
