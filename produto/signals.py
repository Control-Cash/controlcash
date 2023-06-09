from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from produto.models import Produto
from venda.models import Item


@receiver(pre_save, sender=Item)
def restaurar_estoque_antes_de_atualizar_item(sender, instance: Item, **kwargs):
    if instance.id:  # Verifica se o objeto já existe no banco de dados
        item_anterior = Item.objects.get(id=instance.id)

        produto = Produto.objects.get(id=item_anterior.produto.id)
        produto.quantidade_estoque = produto.quantidade_estoque + item_anterior.quantidade
        produto.save()


@receiver(post_save, sender=Item)
def atualizar_estoque_apos_criar_ou_atualizar_item(sender, instance: Item, **kwargs):
    produto = Produto.objects.get(id=instance.produto.id)
    produto.quantidade_estoque = produto.quantidade_estoque - instance.quantidade
    produto.save()


@receiver(pre_delete, sender=Item)
def restaurar_estoque_antes_de_remover_item(sender, instance: Item, **kwargs):
    produto = Produto.objects.get(id=instance.produto.id)
    produto.quantidade_estoque= produto.quantidade_estoque + instance.quantidade
    produto.save()
