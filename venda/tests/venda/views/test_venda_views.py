from django.test import Client, TestCase
from django.urls import reverse_lazy

from venda.models import Cliente, Venda


class ListarVendasView(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('venda:venda_listar')
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.vendas = [
            Venda.objects.create(cliente=self.cliente),
            Venda.objects.create(cliente=self.cliente),
            Venda.objects.create(cliente=self.cliente),
        ]
        self.client = Client()
        self.expected_template = 'venda/venda/listar.html'

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)

    # passa objeto vendas ao template
