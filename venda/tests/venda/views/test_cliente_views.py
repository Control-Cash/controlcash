from django.test import Client, TestCase
from django.urls import reverse_lazy


class CriarClienteView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.target_url = reverse_lazy('venda:cliente_criar')

    def test_view_sends_form_to_template(self):
        """Verifica se a view envia o formulário ao template"""
        response = self.client.get(self.target_url)
        self.assertIsNotNone(
            response.context.get('form'),
            "'form' não é enviado pela view")
