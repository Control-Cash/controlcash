from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from produto.models import Produto


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    # endereco = models.ForeignKey

    def __str__(self) -> str:
        return f"{self.nome}"


class Venda(models.Model):
    STATUS_CHOICES = (
        ('ativa', 'Ativa'),
        ('inativa', 'Inativa'),
        ('finalizada', 'Finalizada')
    )

    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='ativa')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    # vendedor = models.ForeignKey()

    def __str__(self) -> str:
        return f"{self.item_set.count} itens vendidos para {self.cliente} ({self.status})"


class Item(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.01'))])

    def __str__(self) -> str:
        return f"{self.quantidade} {self.produto.nome}"

    def clean(self):
        try:
            if self.quantidade > self.produto.quantidadeEstoque:
                raise ValidationError(
                    f"Há apenas {self.produto.quantidadeEstoque} desse produto em estoque."
                )
        except Item.produto.RelatedObjectDoesNotExist:
            raise ValidationError("Esse produto não existe.")

    def valor_total(self):
        return self.quantidade * self.valor_unitario

    class Meta:
        verbose_name_plural = 'Itens'
