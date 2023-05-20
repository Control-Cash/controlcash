from datetime import date
from decimal import Decimal
from django.test import TestCase
from produto.models import Produto

from venda.models import Cliente, Item, Venda


class ClienteModel(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )

    def test_model_string_representation_is_cliente_nome(self):
        """Verifica se a representação string do modelo 'Cliente' é o seu
        atributo nome"""

        self.assertEqual(
            str(self.cliente),
            f"{self.cliente.nome}",
            "A representação string do modelo 'Cliente' não é o seu atributo nome"
        )


class VendaModel(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)

    def test_model_string_representation_is_venda_details(self):
        """Verifica se a representação string do modelo 'Venda' é uma string com
        detalhes a seu respeito"""

        self.assertEqual(
            str(self.venda),
            f"{self.venda.item_set.count} itens vendidos para {self.venda.cliente} ({self.venda.status})",
            "A representação string do modelo 'Venda' é diferente do esperado"
        )


class ItemModel(TestCase):
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

    def test_model_string_representation_is_item_details(self):
        """Verifica se a representação string do modelo 'Item' é uma string com
        detalhes a seu respeito"""

        self.assertEqual(
            str(self.item),
            f"{self.item.quantidade} {self.item.produto.nome}",
            "A representação string do modelo 'Item' é diferente do esperado"
        )
