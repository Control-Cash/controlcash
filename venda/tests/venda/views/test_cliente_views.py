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

    def test_empty_form_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe dados em
        branco"""
        response = self.client.post(self.target_url, {
            'nome': '',
            'email': ''
        })
        form = response.context.get('form')
        self.assertIsNotNone(form.errors)

    def test_filled_form_saves(self):
        """Verifica se a view cria um cliente quando um post request tem os
        dados corretos"""
        cliente_count = Cliente.objects.count()
        self.client.post(self.target_url, self.form_data)
        self.assertEqual(
            cliente_count + 1,
            Cliente.objects.count(),
            "Um cliente não foi criado com o formulário preechido")

    def test_empty_required_fields_doesnt_save(self):
        """Verifica se a view nao cria um cliente quando um post request tem os
        dados obrigatótios em branco"""
        cliente_count = Cliente.objects.count()
        self.client.post(self.target_url, {
            'nome': '',
            'email': self.form_data.get('email')
        })
        self.assertEqual(
            cliente_count,
            Cliente.objects.count(),
            "Um cliente foi criado com os campos obrigatŕios do formulário em branco")

    def test_empty_optional_fields_saves(self):
        """Verifica se a view cria um cliente quando um post request tem os
        dados opcionais em branco"""
        cliente_count = Cliente.objects.count()
        self.client.post(self.target_url, {
            'nome': self.form_data.get('nome'),
            'email': ''
        })
        self.assertEqual(
            cliente_count + 1,
            Cliente.objects.count(),
            "Um cliente não foi criado com os campos opcionais do formulário em branco")

    def test_empty_required_fields_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe todos os 
        dados obrigatórios em branco"""
        response = self.client.post(self.target_url, {
            'nome': '',
            'email': self.form_data.get('email')
        })
        form = response.context.get('form')
        self.assertIsNotNone(form.errors)
