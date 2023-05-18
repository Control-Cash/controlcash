from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

# Modelo do produto. 
class Produto(models.Model):

    # Campos do modelo

    nome = models.CharField(max_length=150)
    precoVenda = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Preço Venda", validators=[MinValueValidator(0.00)])
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    quantidadeEstoque = models.PositiveIntegerField(verbose_name="Quatidade")
    dataRegistro = models.DateField(auto_now_add = True, verbose_name="Data")

    def __str__(self):
        return self.nome
    
    