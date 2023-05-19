from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from produto.models import Produto
from venda.models import Item


@receiver(pre_save, sender=Item)
def restaurar_estoque(sender, instance, **kwargs):
    if instance.id:  # Verifica se o objeto já existe no banco de dados
        item_anterior = Item.objects.get(id=instance.id)

        produto = Produto.objects.get(id=item_anterior.produto.id)
        produto.quantidadeEstoque = produto.quantidadeEstoque + item_anterior.quantidade
        produto.save()


@receiver(post_save, sender=Item)
def atualizar_estoque(sender, instance, **kwargs):
    produto = Produto.objects.get(id=instance.produto.id)
    produto.quantidadeEstoque = produto.quantidadeEstoque - instance.quantidade
    produto.save()


@receiver(pre_delete, sender=Item)
def restaurar_estoque(sender, instance, **kwargs):
    produto = Produto.objects.get(id=instance.produto.id)
    produto.quantidadeEstoque = produto.quantidadeEstoque + instance.quantidade
    produto.save()
