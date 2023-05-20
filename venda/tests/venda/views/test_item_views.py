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
        self.view_url_name = 'venda:item_remover'

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_response_is_404_when_item_doesnt_exist(self):
        """Verifica se a view retorna 404 quando o atributo 'pk' passado não
        pertence a nenhum item"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)
    # retonra item
    # remove o item
    # redireciona ao remover item
