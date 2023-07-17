from django.db import models
from venda.models import Endereco
# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nome}"