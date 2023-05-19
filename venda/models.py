from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from produto.models import Produto


class Venda(models.Model):
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    # cliente = models.ForeignKey()
    # vendedor = models.ForeignKey()


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
        if self.quantidade > self.produto.quantidadeEstoque:
            raise ValidationError(
                f"Há apenas {self.produto.quantidadeEstoque} desse produto em estoque.")

    def valor_total(self):
        return self.quantidade * self.valor_unitario

    class Meta:
        verbose_name_plural = 'Itens'
