from django.db import models
from django.urls import reverse

# Create your models here.

# Modelo do produto. 
class Produto(models.Model):

    # Campos do modelo

    id = models.BigAutoField(primary_key=True, serialize=True)
    nome = models.CharField(max_length=150)
    precoVenda = models.DecimalField(max_digits=10,decimal_places=2)
    descricao = models.TextField()
    quantidadeEstoque = models.IntegerField()
    dataRegistro = models.DateField()

    def __str__(self):
        return self.nome
    
    