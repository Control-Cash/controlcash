from django.test import TestCase

from fornecedor.models import Fornecedor
from venda.models import Endereco


class FornecedorModelTest(TestCase):
    def setUp(self) -> None:
        self.fornecedor = Fornecedor.objects.create(
            nome='Bolachas samanau',
            email="samanau@bolachas.com",
            endereco=Endereco.objects.create(
                cep='12345678',
                numero=10,
                rua='Rua Exemplo',
                bairro='Bairro Exemplo',
                cidade='Cidade Exemplo',
                estado='Estado Exemplo',
                pais='Brasil',
                complemento='Complemento Exemplo'
            )
        )

    def test_model_string_representation_is_as_expected(self):
        """Verifica se a representação string do modelo 'Fornecedor' é o esperado"""

        self.assertEqual(
            str(self.fornecedor),
            f"{self.fornecedor.nome}",
            "A representação string do modelo 'Fornecedor' não está correta"
        )
