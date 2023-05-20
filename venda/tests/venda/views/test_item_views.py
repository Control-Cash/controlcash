from datetime import date
from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse_lazy

from produto.models import Produto
from venda.forms import EditarItemVendaForm
from venda.models import Cliente, Item, Venda


class EditarQuantidadeItemView(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)
        self.produto = Produto.objects.create(
            nome='sandalia',
            precoVenda=Decimal(20),
            quantidadeEstoque=5,
            dataRegistro=date(2023, 2, 1)
        )
        self.item = Item.objects.create(
            produto=self.produto,
            quantidade=1,
            venda=self.venda
        )
        self.expected_template = 'venda/item/editar.html'
        self.view_url_name = 'venda:item_editar'
        self.success_redirect_url_name = 'venda:venda_detalhar'
        self.expected_form_type = EditarItemVendaForm
        self.client = Client()

    def test_view_returns_item_to_template(self):
        """Verifica se a view passa o item que o usuário deseja editar para o
        template"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertIsNotNone(response.context.get('item'))
        self.assertIsInstance(response.context.get('item'), Item)

    def test_returns_404_when_item_doesnt_exist(self):
        """Verifica se a view response com 404 quando o item solicitado não
        existe"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_uses_expected_form_type(self):
        """Verifica se a view passa para o template o formulário correto"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertIsInstance(response.context.get(
            'form'), self.expected_form_type)

    def test_view_uses_expected_template(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_item_not_updated_when_quantidade_equal_zero(self):
        """Verifica se a view não atualiza o item quando a quantidade passada é
        igual a 0"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.item.id
                }
            ),
            {
                'quantidade': 0
            }
        )
        form_errors = response.context.get('form').errors
        after_request_item = Item.objects.get(id=self.item.id)

        self.assertEqual(after_request_item, self.item)
        self.assertIsNotNone(form_errors)

    def test_item_not_updated_when_quantidade_is_less_than_zero(self):
        """Verifica se a view não atualiza o item quando a quantidade passada é
        menor que zero"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.item.id
                }
            ),
            {
                'quantidade': -1
            }
        )
        form_errors = response.context.get('form').errors
        after_request_item = Item.objects.get(id=self.item.id)

        self.assertEqual(after_request_item, self.item)
        self.assertIsNotNone(form_errors)

    def test_item_updates_when_quantidade_is_greater_than_zero(self):
        """Verifica se a view atualiza o item quando a quantidade passada é
        maior que zero"""

        nova_quantidade = 3
        self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.item.id
                }
            ),
            {
                'quantidade': nova_quantidade
            }
        )
        updated_item = Item.objects.get(id=self.item.id)

        self.assertEqual(updated_item.quantidade, nova_quantidade)

    # redireciona ao salvar para a pagina correta


class RemoverItemView(TestCase):
    def setUp(self) -> None:
        self.cliente = Cliente.objects.create(
            nome='João',
            email="joao@gmail.com"
        )
        self.venda = Venda.objects.create(cliente=self.cliente)
        self.produto = Produto.objects.create(
            nome='sandalia',
            precoVenda=Decimal(20),
            quantidadeEstoque=5,
            dataRegistro=date(2023, 2, 1)
        )
        self.item = Item.objects.create(
            produto=self.produto,
            quantidade=1,
            venda=self.venda
        )
        self.expected_template = 'venda/item/remover.html'
        self.client = Client()
        self.view_url_name = 'venda:item_remover'
        self.success_redirect_url_name = 'venda:venda_detalhar'

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_response_is_404_when_item_doesnt_exist(self):
        """Verifica se a view retorna 404 quando o atributo 'pk' passado não
        pertence a nenhum item"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_sends_item_to_template(self):
        """Verifica se a view envia ao template o item associado ao atributo
        'pk' passado na request"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))
        item_recebido = response.context.get('item')

        self.assertIsNotNone(item_recebido)
        self.assertIsInstance(item_recebido, Item)
        self.assertEqual(self.item, item_recebido)

    def removes_item_on_post_request(self):
        """Verifica se a view realiza a remoção do item do banco de dados"""

        initial_count = Item.objects.count()
        self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertEqual(initial_count - 1, Item.objects.count())

    def test_redirects_to_correct_page_after_delete(self):
        """Verifica se a view redireciona para a página correta após excluir o
        item"""

        response = self.client.post(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.item.id
            }
        ))

        self.assertRedirects(
            response,
            reverse_lazy(
                self.success_redirect_url_name,
                kwargs={
                    'pk': self.venda.id
                }
            ),
            302,
            200
        )
