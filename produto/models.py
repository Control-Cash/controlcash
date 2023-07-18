from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

# Modelo do produto.


class Produto(models.Model):

    # Campos do modelo

    nome = models.CharField(max_length=150)
    preco_venda = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="preço", validators=[MinValueValidator(0.00)])
    descricao = models.TextField(
        blank=True, null=True, verbose_name="descrição")
    quantidade_estoque = models.PositiveIntegerField(
        verbose_name="quantidade em estoque")
    data_registro = models.DateField(auto_now_add=True, verbose_name="data")

    def __str__(self):
        return self.nome
