from datetime import date
from decimal import Decimal
from django.test import Client, TestCase
from django.urls import reverse_lazy
from produto.models import Produto

from venda.models import Cliente, Item, Venda


class RemoverItemView(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)
        self.produto = Produto.objects.create(
            nome='sandalia',
            precoVenda=Decimal(20),
            quantidadeEstoque=5,
            dataRegistro=date(2023, 2, 1)
        )
        self.item = Item.objects.create(
            produto=self.produto,
            quantidade=1,
            venda=self.venda
        )
        self.expected_template = 'venda/item/remover.html'
        self.client = Client()

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            'venda:item_remover',
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    # retorna 404 quando o item nao existe
    # retonra item
    # remove o item
