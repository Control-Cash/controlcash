from django.test import Client, TestCase
from django.urls import reverse_lazy

from despesa.models import Despesa


class ListarDespesasViewTest(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('despesa:despesa_listar')
        self.despesas = [
            Despesa.objects.create(nome="Depesa 1", valor=10.51),
            Despesa.objects.create(nome="Depesa 2", valor=10.52),
            Despesa.objects.create(nome="Depesa 3", valor=10.53),
        ]
        self.client = Client()
        self.expected_template = 'despesa/listar.html'

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)

    def test_view_sends_despesas_to_template(self):
        """Verifica se a view envia os objetos Despesa para o template"""

        response = self.client.get(self.target_url)
        despesas = response.context.get('despesas')

        self.assertIsNotNone(despesas)
        self.assertIn(self.despesas[0], despesas)
        self.assertIn(self.despesas[1], despesas)
        self.assertIn(self.despesas[2], despesas)
        self.assertIsInstance(self.despesas[0], Despesa)
        self.assertIsInstance(self.despesas[1], Despesa)
        self.assertIsInstance(self.despesas[2], Despesa)
