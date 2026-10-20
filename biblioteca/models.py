from django.db import models

# Create your models here.
class Autor(models.Model):
    nome= models.CharField(max_length=100)
    nacionalidade= models.CharField(max_length=100)
