from datetime import date
from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse_lazy

from produto.models import Produto
from venda.forms import CriarVendaForm, ItemVendaForm
from venda.models import Cliente, Venda


class ListarVendasViewTest(TestCase):
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

    def test_view_sends_vendas_to_template(self):
        """Verifica se a view envia os objetos Venda para o template"""

        response = self.client.get(self.target_url)
        vendas = response.context.get('vendas')

        self.assertIsNotNone(vendas)
        self.assertIn(self.vendas[0], vendas)
        self.assertIn(self.vendas[1], vendas)
        self.assertIn(self.vendas[2], vendas)
        self.assertIsInstance(self.vendas[0], Venda)
        self.assertIsInstance(self.vendas[1], Venda)
        self.assertIsInstance(self.vendas[2], Venda)


class CriarVendaViewTest(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('venda:venda_criar')
        self.expected_template = 'venda/venda/criar.html'
        self.expected_form_class = CriarVendaForm
        self.expected_url_redirect_name = 'venda:venda_detalhar'
        self.client = Client()
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.produto = Produto.objects.create(
            nome='Celular',
            precoVenda=Decimal(1000),
            quantidadeEstoque=10,
            dataRegistro=date(2023, 2, 10)
        )

    def test_correct_form_in_context(self):
        """Verifica se a view envia um formulário para o template e se esse formulário é da classe correta"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertIsInstance(form, self.expected_form_class)

    def test_correct_template_rendered(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(response, self.expected_template)

    def test_doesnt_create_venda_when_cliente_is_none(self):
        """Verifica se a venda não é criada quando o cliente não é passado para a view"""

        form_data = {
            'produto': self.produto.id,
            'quantidade': 1,
            'cliente': ''
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Venda.objects.exists())

    def test_redirects_to_correct_page_on_save(self):
        """Verifica se a view redireciona para a página correta após salvar a venda"""

        form_data = {
            'cliente': self.cliente.id,
            'produto': self.produto.id,
            'quantidade': 1
        }
        response = self.client.post(self.target_url, data=form_data)
        venda_criada = Venda.objects.last()

        self.assertRedirects(
            response,
            reverse_lazy(
                self.expected_url_redirect_name,
                kwargs={
                    'pk': venda_criada.id
                }
            ),
            302,
            200
        )

    def test_doesnt_create_venda_when_produto_is_none(self):
        """Verifica se a venda não é criada quando o produto não é passado para a view"""

        form_data = {
            'cliente': self.cliente.id,
            'quantidade': 1,
            'produto': ''
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Venda.objects.exists())

    def test_creates_venda_when_all_data_is_given(self):
        """Verifica se a venda é criada quando todos os dados são passados para a view"""

        form_data = {
            'cliente': self.cliente.id,
            'quantidade': 1,
            'produto': self.produto.id
        }
        self.client.post(self.target_url, data=form_data)

        self.assertTrue(Venda.objects.exists())
        self.assertEqual(Venda.objects.last().cliente.id, form_data['cliente'])

    def test_view_return_form_errors_when_some_data_is_missing(self):
        """Verifica se a venda retorna erros de fomrulário quando recebe dados incompletos"""

        form_data = {
            'produto': '',
            'quantidade': '',
            'cliente': ''
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'].errors)

    def test_doesnt_create_venda_when_quantidade_greater_than_estoque(self):
        """Verifica se a venda não é criada quando o quantidade do produto é maior que o estoque"""

        form_data = {
            'cliente': self.cliente.id,
            'quantidade': 100000,
            'produto': self.produto.id
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertFalse(Venda.objects.exists())
        self.assertIsNotNone(response.context['form'].errors)

    def test_intial_form_is_empty(self):
        """Verifica se a view envia um formulário vazio para o template"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertIsNone(form.initial.get('produto'))
        self.assertIsNone(form.initial.get('quantidade'))
        self.assertIsNone(form.initial.get('cliente'))

    def test_form_fields_are_filled_with_previous_values(self):
        """Verifica se a view envia os campos do formulário preenchidos com os valores anteriores em caso de erro de validação"""

        form_data = {
            'produto': self.produto.id,
            'quantidade': 1,
            'cliente': ''
        }
        response = self.client.post(self.target_url, data=form_data)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertEqual(
            form['produto'].value(),
            str(form_data.get('produto'))
        )

        self.assertEqual(
            form['cliente'].value(),
            form_data['cliente']
        )


class DesativarVendaViewTest(TestCase):
    def setUp(self) -> None:
        self.expected_template = 'venda/venda/desativar.html'
        self.target_url_name = 'venda:venda_desativar'
        self.expected_url_redirect_name = 'venda:venda_detalhar'
        self.client = Client()
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.produto = Produto.objects.create(
            nome='Celular',
            precoVenda=Decimal(1000),
            quantidadeEstoque=10,
            dataRegistro=date(2023, 2, 10)
        )
        self.venda = Venda.objects.create(
            cliente=self.cliente
        )
        self.target_url = reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': self.venda.id
            }
        )

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)

    def test_view_alters_venda_when_post_request_is_submitted(self):
        """Verifica se a view desativa a venda quando é submetida"""

        self.client.post(self.target_url)
        self.venda.refresh_from_db()

        self.assertEqual(self.venda.status, 'inativa')

    def test_view_redirects_to_correct_page_after_update(self):
        """Verifica se a view redireciona para a página correta após ser submetida"""

        response = self.client.post(self.target_url)

        self.assertRedirects(
            response,
            reverse_lazy(
                self.expected_url_redirect_name,
                kwargs={
                    'pk': self.venda.id
                }
            ),
            302,
            200
        )

    def test_view_sends_correct_venda_to_template(self):
        """Verifica se a view passa o objeto venda solicitado"""

        response = self.client.get(self.target_url)
        venda = response.context.get('venda')

        self.assertIsNotNone(venda)
        self.assertIsInstance(venda, Venda)
        self.assertEqual(venda.id, self.venda.id)

    def test_view_returns_404_when_venda_is_not_found(self):
        """Verifica se a view retorna 404 quando o objeto venda solicitado não existe"""

        response = self.client.get(reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)


class ReativarVendaViewTest(TestCase):
    def setUp(self) -> None:
        self.expected_template = 'venda/venda/reativar.html'
        self.target_url_name = 'venda:venda_reativar'
        self.expected_url_redirect_name = 'venda:venda_detalhar'
        self.client = Client()
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.produto = Produto.objects.create(
            nome='Celular',
            precoVenda=Decimal(1000),
            quantidadeEstoque=10,
            dataRegistro=date(2023, 2, 10)
        )
        self.venda = Venda.objects.create(
            cliente=self.cliente,
            status=Venda.STATUS_CHOICES[1][0]
        )
        self.target_url = reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': self.venda.id
            }
        )

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)

    def test_view_alters_venda_when_post_request_is_submitted(self):
        """Verifica se a view reativa a venda quando é submetida"""

        self.client.post(self.target_url)
        self.venda.refresh_from_db()

        self.assertEqual(self.venda.status, 'ativa')

    def test_view_redirects_to_correct_page_after_update(self):
        """Verifica se a view redireciona para a página correta após ser submetida"""

        response = self.client.post(self.target_url)

        self.assertRedirects(
            response,
            reverse_lazy(
                self.expected_url_redirect_name,
                kwargs={
                    'pk': self.venda.id
                }
            ),
            302,
            200
        )

    def test_view_sends_correct_venda_to_template(self):
        """Verifica se a view passa o objeto venda solicitado"""

        response = self.client.get(self.target_url)
        venda = response.context.get('venda')

        self.assertIsNotNone(venda)
        self.assertIsInstance(venda, Venda)
        self.assertEqual(venda.id, self.venda.id)

    def test_view_returns_404_when_venda_is_not_found(self):
        """Verifica se a view retorna 404 quando o objeto venda solicitado não existe"""

        response = self.client.get(reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)


class FinalizarVendaViewTest(TestCase):
    def setUp(self) -> None:
        self.expected_template = 'venda/venda/finalizar.html'
        self.target_url_name = 'venda:venda_finalizar'
        self.expected_url_redirect_name = 'venda:venda_detalhar'
        self.client = Client()
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.produto = Produto.objects.create(
            nome='Celular',
            precoVenda=Decimal(1000),
            quantidadeEstoque=10,
            dataRegistro=date(2023, 2, 10)
        )
        self.venda = Venda.objects.create(
            cliente=self.cliente,
        )
        self.target_url = reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': self.venda.id
            }
        )

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)

    def test_view_alters_venda_when_post_request_is_submitted(self):
        """Verifica se a view reativa a venda quando é submetida"""

        self.client.post(self.target_url)
        self.venda.refresh_from_db()

        self.assertEqual(self.venda.status, 'finalizada')

    def test_view_redirects_to_correct_page_after_update(self):
        """Verifica se a view redireciona para a página correta após ser submetida"""

        response = self.client.post(self.target_url)

        self.assertRedirects(
            response,
            reverse_lazy(
                self.expected_url_redirect_name,
                kwargs={
                    'pk': self.venda.id
                }
            ),
            302,
            200
        )

    def test_view_sends_correct_venda_to_template(self):
        """Verifica se a view passa o objeto venda solicitado"""

        response = self.client.get(self.target_url)
        venda = response.context.get('venda')

        self.assertIsNotNone(venda)
        self.assertIsInstance(venda, Venda)
        self.assertEqual(venda.id, self.venda.id)

    def test_view_returns_404_when_venda_is_not_found(self):
        """Verifica se a view retorna 404 quando o objeto venda solicitado não existe"""

        response = self.client.get(reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

class DetalharVendaViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.expected_template = 'venda/venda/detalhar.html'
        self.target_url_name = 'venda:venda_detalhar'
        self.expected_url_redirect_name = 'venda:venda_detalhar'
        self.expected_form_type = ItemVendaForm
        self.cliente = Cliente.objects.create(nome='João Silva')
        self.produto = Produto.objects.create(
            nome='Celular',
            precoVenda=Decimal(1000),
            quantidadeEstoque=10,
            dataRegistro=date(2023, 2, 10)
        )
        self.venda = Venda.objects.create(
            cliente=self.cliente,
        )
        self.target_url = reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': self.venda.id
            }
        )

    def test_view_sends_venda_requested(self):
        """A view envia a venda correspondente a id passada"""

        response = self.client.get(self.target_url)
        venda = response.context['venda']

        self.assertIsNotNone(venda)
        self.assertIsInstance(venda, Venda)
        self.assertEqual(venda.id, self.venda.id)

    def test_view_returns_404_when_venda_doesnt_exist(self):
        """A view retorna 404 quando a id passada não corresponde a uma venda"""

        response = self.client.get(reverse_lazy(
            self.target_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_uses_expected_temlpate(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.expected_template)
        
    # form correto é enviado
    # adiciona item quando preenchido corretamente
    # nao adiciona item quando campo obrigatorio vai vazio
    # quando adiciona o item redireciona para a url esperada
    # quando o item ja está na venda a quantidade é somada ao inves de criar um novo item igual
    # campos do form iniciam vazios
    # quando há erro os campos carregam com os valores anteriores