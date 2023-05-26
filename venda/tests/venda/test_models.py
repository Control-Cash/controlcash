from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from produto.models import Produto
from venda.models import Cliente, Item, Venda


class ClienteModelTest(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )

    def test_model_string_representation_is_cliente_nome(self):
        """Verifica se a representação string do modelo 'Cliente' é o seu atributo nome"""

        self.assertEqual(
            str(self.cliente),
            f"{self.cliente.nome}",
            "A representação string do modelo 'Cliente' não é o seu atributo nome"
        )


class VendaModelTest(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)

    def test_model_string_representation_is_venda_details(self):
        """Verifica se a representação string do modelo 'Venda' é uma string com detalhes a seu respeito"""

        self.assertEqual(
            str(self.venda),
            f"{self.venda.item_set.count} itens vendidos para {self.venda.cliente} ({self.venda.status})",
            "A representação string do modelo 'Venda' é diferente do esperado"
        )


class ItemModelTest(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)
        self.produto = Produto.objects.create(
            nome='sandalia',
            preco_venda=Decimal(20),
            quantidade_estoque=5
        )
        self.item = Item.objects.create(
            produto=self.produto,
            quantidade=1,
            venda=self.venda
        )

    def test_model_string_representation_is_item_details(self):
        """Verifica se a representação string do modelo 'Item' é uma string com detalhes a seu respeito"""

        self.assertEqual(
            str(self.item),
            f"{self.item.quantidade} {self.item.produto.nome}",
            "A representação string do modelo 'Item' é diferente do esperado"
        )

    def test_model_raises_error_when_quantidade_is_greater_than_estoque(self):
        """Verifica se o modelo lança um erro ao tentar criar um item com uma quatidade maior do que o estoque do produto"""

        item = Item(
            quantidade=self.produto.quantidade_estoque + 1,
            produto=self.produto,
            venda=self.venda
        )

        self.assertRaises(ValidationError, item.full_clean)

    def test_valor_total_returns_multiplication_of_quantidade_and_valor_unitario(self):
        """Verifica se a chamada do método valor_total retorna o preço unitário do item multiplicado por sua quantidade"""

        item = Item.objects.create(
            quantidade=2,
            produto=self.produto,
            venda=self.venda
        )

        self.assertEqual(
            item.quantidade *
            item.valor_unitario, item.valor_total(),
            "O método 'valor_total' não retornou o valor esperado"
        )
