from django.test import Client, TestCase
from django.urls import reverse_lazy

from venda.forms import ClienteForm
from venda.models import Cliente


class CriarClienteView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.target_url = reverse_lazy('venda:cliente_criar')
        self.form_data = {
            'nome': 'José Silva',
            'email': 'josesilva@gmail.com'
        }

    def test_view_sends_form_to_template(self):
        """Verifica se a view envia o formulário ao template"""
        response = self.client.get(self.target_url)
        self.assertIsNotNone(
            response.context.get('form'),
            "'form' não é enviado pela view")

    def test_form_sended_to_template_is_cliente_form(self):
        """Verifica se a view envia o formulário correto ao template"""
        response = self.client.get(self.target_url)
        self.assertIsInstance(
            response.context.get('form'),
            ClienteForm,
            "'form' enviado pela view não é 'ClienteForm'")

    def test_empty_form_doesnt_save(self):
        """Verifica se a view nao cria um cliente quando um post request tem os
        dados em branco"""
        cliente_count = Cliente.objects.count()
        self.client.post(self.target_url, {
            'nome': '',
            'email': ''
        })
        self.assertEqual(cliente_count, Cliente.objects.count(
        ), "Um cliente foi criado com o formulário em branco")
