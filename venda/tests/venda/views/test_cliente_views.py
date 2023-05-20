from django.db.models import QuerySet
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
        self.expeted_template = 'venda/cliente/criar.html'

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

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderizacao"""
        response = self.client.get(self.target_url)
        self.assertTemplateUsed(
            response,
            self.expeted_template,
            'A view usou um template diferente do esperado')

    def test_successful_post_request_redirects(self):
        """Verifica se a view redireciona quando uma solicitação post é enviada
        corretamente com todos os dados"""
        response = self.client.post(self.target_url, self.form_data)
        self.assertEqual(
            response.status_code,
            302,
            'A view não redirecionou após post request bem sucedido')

    def test_successful_post_request_redirects_to_expected_url(self):
        """Verifica se a view redireciona para a url correta quando uma
        solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)
        cliente_criado = Cliente.objects.last()
        reverse_lazy()

        self.assertRedirects(
            response,
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': cliente_criado.id
                }
            ),
            302,
            200)


class ListarClientesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.target_url = reverse_lazy('venda:cliente_listar')
        self.clientes_data = [
            {
                'nome': 'José Silva',
                'email': 'josesilva@gmail.com'
            },
            {
                'nome': 'João Silva',
                'email': 'joaosilva@gmail.com'
            },
            {
                'nome': 'Maria Santos',
                'email': 'mariasantos@outlook.com'
            },
        ]
        self.expeted_template = 'venda/cliente/listar.html'

    def test_view_sends_clientes_to_template(self):
        """Verifica se a view envia uma variavel 'clientes' ao template"""

        response = self.client.get(self.target_url)
        self.assertIsNotNone(
            response.context.get('clientes'),
            "'clientes' não é enviado pela view")
