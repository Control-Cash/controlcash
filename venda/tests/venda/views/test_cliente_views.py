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
        self.expected_template = 'venda/cliente/criar.html'

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
        """Verifica se a view não cria um cliente quando um post request tem os
        dados em branco"""

        cliente_count = Cliente.objects.count()
        self.client.post(self.target_url, {
            'nome': '',
            'email': ''
        })

        self.assertEqual(
            cliente_count,
            Cliente.objects.count(),
            "Um cliente foi criado com o formulário em branco"
        )

    def test_empty_form_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe dados em
        branco"""

        response = self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': ''
            }
        )
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
        self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': self.form_data.get('email')
            }
        )

        self.assertEqual(
            cliente_count,
            Cliente.objects.count(),
            "Um cliente foi criado com os campos obrigatŕios do formulário em branco")

    def test_empty_optional_fields_saves(self):
        """Verifica se a view cria um cliente quando um post request tem os
        dados opcionais em branco"""

        cliente_count = Cliente.objects.count()
        self.client.post(
            self.target_url,
            {
                'nome': self.form_data.get('nome'),
                'email': ''
            }
        )

        self.assertEqual(
            cliente_count + 1,
            Cliente.objects.count(),
            "Um cliente não foi criado com os campos opcionais do formulário em branco"
        )

    def test_empty_required_fields_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe todos os 
        dados obrigatórios em branco"""

        response = self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': self.form_data.get('email')
            }
        )
        form = response.context.get('form')

        self.assertIsNotNone(form.errors)

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderizacao"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )

    def test_successful_post_request_redirects(self):
        """Verifica se a view redireciona quando uma solicitação post é enviada
        corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)

        self.assertEqual(
            response.status_code,
            302,
            'A view não redirecionou após post request bem sucedido'
        )

    def test_successful_post_request_redirects_to_expected_url(self):
        """Verifica se a view redireciona para a url correta quando uma
        solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)
        cliente_criado = Cliente.objects.last()

        self.assertRedirects(
            response,
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': cliente_criado.id
                }
            ),
            302,
            200
        )


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
        self.expected_template = 'venda/cliente/listar.html'

    def test_view_sends_clientes_to_template(self):
        """Verifica se a view envia uma variavel 'clientes' ao template"""

        response = self.client.get(self.target_url)

        self.assertIsNotNone(
            response.context.get('clientes'),
            "'clientes' não é enviado pela view"
        )

    def test_clientes_sended_to_template_contains_clientes_data(self):
        """Verifica se a view envia os dados dos clientes ao template"""

        Cliente.objects.create(
            nome=self.clientes_data[0].get('nome'),
            email=self.clientes_data[0].get('email'),
        )

        response = self.client.get(self.target_url)
        clientes = response.context.get('clientes')

        self.assertIsInstance(
            clientes,
            QuerySet,
            "'clientes' enviado pela view não é conjunto de modelos"
        )
        self.assertTrue(
            all(isinstance(cliente, Cliente) for cliente in clientes),
            "Os objetos retornados não são do modelo 'Cliente'"
        )

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )

    def test_all_clients_are_sended_to_template(self):
        """Verifica se a view envia todos os clientes ao template"""

        cliente1 = Cliente.objects.create(
            nome=self.clientes_data[0].get('nome'),
            email=self.clientes_data[0].get('email'),
        )
        cliente2 = Cliente.objects.create(
            nome=self.clientes_data[1].get('nome'),
            email=self.clientes_data[1].get('email'),
        )
        cliente3 = Cliente.objects.create(
            nome=self.clientes_data[2].get('nome'),
            email=self.clientes_data[2].get('email'),
        )

        response = self.client.get(self.target_url)
        clientes = response.context.get('clientes')

        self.assertIn(cliente1, clientes)
        self.assertIn(cliente2, clientes)
        self.assertIn(cliente3, clientes)


class DetalharClienteView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.expected_template = 'venda/cliente/detalhar.html'
        self.cliente_criado = Cliente.objects.create(
            nome='José Silva',
            email='josesilva@gmail.com'
        )

    def test_view_returns_cliente_requested(self):
        """Veriica se a view retorna ao template o cliente solicitado"""

        response = self.client.get(
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': self.cliente_criado.id
                }
            )
        )
        cliente_retornado = response.context.get('cliente')

        self.assertIsNotNone(
            cliente_retornado,
            "A view não retorna a variável 'cliente'"
        )
        self.assertEqual(
            self.cliente_criado,
            cliente_retornado,
            "A view não retornou o cliente solicitado"
        )

    def test_view_returns_404_when_cliente_is_unknown(self):
        """Verifica se a view retorna uma resposta 404 quando o cliente
        solicitado não existe"""

        response = self.client.get(
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': 50
                }
            )
        )

        self.assertIsNone(response.context.get('cliente'))
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': self.cliente_criado.id
                }
            )
        )

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )


class EditarClienteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.expected_template = 'venda/cliente/editar.html'
        self.cliente_criado = Cliente.objects.create(
            nome='João Silva',
            email='joaosilva@gmail.com'
        )
        self.form_data = {
            'nome': 'João Silva 2',
            'email': 'joaosilva@outlook.com'
        }
        self.target_url = reverse_lazy(
            'venda:cliente_editar',
            kwargs={
                'pk': self.cliente_criado.id
            }
        )

    def test_view_sends_form_to_template(self):
        """Verifica se a view envia o formulário ao template"""

        response = self.client.get(self.target_url)

        self.assertIsNotNone(
            response.context.get('form'),
            "'form' não é enviado pela view"
        )

    def test_form_sended_to_template_is_cliente_form(self):
        """Verifica se a view envia o formulário correto ao template"""

        response = self.client.get(self.target_url)

        self.assertIsInstance(
            response.context.get('form'),
            ClienteForm,
            "'form' enviado pela view não é 'ClienteForm'"
        )

    def test_empty_form_doesnt_save(self):
        """Verifica se a view não salva os dados quando um post request tem os
        dados em branco"""

        self.client.post(self.target_url, {
            'nome': '',
            'email': ''
        })
        cliente_atualizado = Cliente.objects.get(id=self.cliente_criado.id)

        self.assertEqual(
            cliente_atualizado.nome,
            self.cliente_criado.nome,
            "O nome do cliente foi alterado com o formulário em branco"
        )
        self.assertEqual(
            cliente_atualizado.email,
            self.cliente_criado.email,
            "O email do cliente foi alterado com o formulário em branco"
        )

    def test_filled_form_saves(self):
        """Verifica se a view salva os dados quando um post request tem os
        dados corretos"""

        self.client.post(self.target_url, self.form_data)
        self.cliente_criado.refresh_from_db()

        self.assertEqual(
            self.cliente_criado.nome,
            self.form_data.get('nome'),
            "O nome do cliente não foi alterado com o formulário preenchido corretamente"
        )
        self.assertEqual(
            self.cliente_criado.email,
            self.form_data.get('email'),
            "O email do cliente não foi alterado com o formulário preenchido corretamente"
        )

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )

    def test_view_returns_404_when_cliente_is_unknown(self):
        """Verifica se a view retorna uma resposta 404 quando o cliente
        solicitado não existe"""

        response = self.client.get(
            reverse_lazy(
                'venda:cliente_editar',
                kwargs={
                    'pk': 50
                }
            )
        )

        self.assertIsNone(response.context.get('form'))
        self.assertEqual(response.status_code, 404)

    def test_empty_required_fields_doesnt_save(self):
        """Verifica se a view nao atualiza um cliente quando um post request tem
        os dados obrigatótios em branco"""

        self.client.post(self.target_url, {'nome': ''})
        cliente_atualizado = Cliente.objects.get(id=self.cliente_criado.id)

        self.assertEqual(
            cliente_atualizado.nome,
            self.cliente_criado.nome,
            "O cliente foi atualizado com os campos obrigatŕios do formulário em branco"
        )

    def test_empty_optional_fields_saves(self):
        """Verifica se a view atualiza um cliente quando um post request tem os
        dados opcionais em branco"""

        self.client.post(self.target_url, {'nome': self.form_data.get('nome')})
        cliente_atualizado = Cliente.objects.get(id=self.cliente_criado.id)

        self.assertEqual(
            cliente_atualizado.nome,
            self.form_data.get('nome'),
            "Um cliente não foi atualizado com os campos opcionais do formulário em branco"
        )

    def test_empty_required_fields_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe todos os 
        dados obrigatórios em branco"""

        response = self.client.post(self.target_url, {'nome': ''})
        form = response.context.get('form')

        self.assertIsNotNone(form.errors)

    def test_redirects_to_correct_page_on_update(self):
        """Verifica se a view redireciona para a url correta quando uma
        solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)

        self.assertRedirects(
            response,
            reverse_lazy(
                'venda:cliente_detalhar',
                kwargs={
                    'pk': self.cliente_criado.id
                }
            ),
            302,
            200
        )

    def test_form_loads_with_values_from_model(self):
        """Verifica se a view envia o formulário com os campos preenchidos com
        os valores atuais salvos no banco de dados para o template"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertEqual(form.initial.get('nome'), self.cliente_criado.nome)
        self.assertEqual(form.initial.get('email'), self.cliente_criado.email)
