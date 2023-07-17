from django.test import TestCase

from despesa.models import Despesa


class DespesaModelTest(TestCase):
    def setUp(self) -> None:
        self.despesa = Despesa.objects.create(
            nome='Despesa teste',
            valor=10.52,
            vencimento='2023-07-19'
        )

    def test_model_string_representation(self):
        """Verifica se a representação string do modelo 'Despesa' é o seu atributo nome"""

        self.assertEqual(
            str(self.despesa),
            f"{self.despesa.nome}",
            "A representação string do modelo 'Despesa' não é o seu atributo nome"
        )
