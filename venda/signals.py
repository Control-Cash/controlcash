
from django.db.models.signals import pre_save
from django.dispatch import receiver

from venda.models import Item


@receiver(pre_save, sender=Item)
def preencher_valor_unitario(sender, instance, **kwargs):
    if not instance.valor_unitario:
        instance.valor_unitario = instance.produto.precoVenda
