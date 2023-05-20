from django.test import TestCase

from venda.models import Cliente


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
