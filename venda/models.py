from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from produto.models import Produto

class Endereco(models.Model):
    cep = models.CharField(max_length=8, default='12345678')
    numero = models.PositiveIntegerField(verbose_name='numero')
    rua = models.CharField(max_length=150, verbose_name='rua')
    bairro = models.CharField(max_length=150, verbose_name='bairro')
    cidade = models.CharField(max_length=150,verbose_name='cidade')
    estado = models.CharField(max_length=150,verbose_name='estado')
    pais = models.CharField(max_length=150, verbose_name='país', default='Brasil')
    complemento = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.numero, self.cidade, self.bairro}"

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    # TODO adicionar foreign key endereco
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=None, null=True, blank=True)
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
    # TODO adicionar foreign key vendedor

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
            if self.quantidade and self.produto.quantidade_estoque:
                if self.quantidade > self.produto.quantidade_estoque:
                    raise ValidationError(
                        f"Há apenas {self.produto.quantidade_estoque} desse produto em estoque."
                    )
        except Item.produto.RelatedObjectDoesNotExist:
            raise ValidationError("Esse produto não existe.")

    def valor_total(self):
        return self.quantidade * self.valor_unitario

    class Meta:
        verbose_name_plural = 'Itens'
