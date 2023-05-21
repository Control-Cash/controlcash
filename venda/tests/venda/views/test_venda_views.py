from datetime import date
from decimal import Decimal
from django.test import Client, TestCase
from django.urls import reverse_lazy
from venda.forms import CriarVendaForm

from venda.models import Cliente, Item, Venda
from produto.models import Produto


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


class CriarVendaView(TestCase):
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
        """Verifica se a view envia um formulário para o template e se esse
        formulário é da classe correta"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertIsInstance(form, self.expected_form_class)

    def test_correct_template_rendered(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(response, self.expected_template)

    def test_doesnt_create_venda_when_cliente_is_none(self):
        """Verifica se a venda não é criada quando o cliente não é passado para
        a view"""

        form_data = {
            'produto': self.produto.pk,
            'quantidade': 1,
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Venda.objects.exists())

    # nao cria venda sem item
    # redireciona para a url correta ao salvar
    # cria venda quando os dados tao corretos
    # retorna erros no form quando vai preenchido errado
    # nao cria venda quando a quantidade do item é maior que o estoque de produto
    # form inicial carrega com os campos vazios
    # form apos erro de validacao renderiza com os campos preenchidos anteriormente
