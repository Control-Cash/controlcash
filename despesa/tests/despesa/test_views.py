from django.test import Client, TestCase
from django.urls import reverse_lazy

from despesa.forms import DespesaForm
from despesa.models import Despesa


class ListarDespesasViewTest(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('despesa:despesa_listar')
        self.despesas = [
            Despesa.objects.create(
                nome="Depesa 1", valor=10.51, vencimento='2023-07-19'),
            Despesa.objects.create(
                nome="Depesa 2", valor=10.52, vencimento='2023-07-19'),
            Despesa.objects.create(
                nome="Depesa 3", valor=10.53, vencimento='2023-07-19'),
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
        despesas = response.context.get('page_obj').object_list

        self.assertIsNotNone(despesas)
        self.assertIn(self.despesas[0], despesas)
        self.assertIn(self.despesas[1], despesas)
        self.assertIn(self.despesas[2], despesas)
        self.assertIsInstance(self.despesas[0], Despesa)
        self.assertIsInstance(self.despesas[1], Despesa)
        self.assertIsInstance(self.despesas[2], Despesa)


class CriarDespesaViewTest(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('despesa:despesa_criar')
        self.expected_template = 'despesa/criar.html'
        self.expected_form_class = DespesaForm
        self.expected_url_redirect_name = 'despesa:despesa_listar'
        self.client = Client()

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

    def test_doesnt_create_despesa_when_nome_is_none(self):
        """Verifica se a despesa não é criada quando o nome não é passado para a view"""

        form_data = {
            'nome': '',
            'valor': 1,
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Despesa.objects.exists())

    def test_redirects_to_correct_page_on_save(self):
        """Verifica se a view redireciona para a página correta após salvar a despesa"""

        form_data = {
            'nome': "Despesa 1",
            'valor': 10.51,
            'vencimento': '2023-07-19'
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertRedirects(
            response,
            reverse_lazy(self.expected_url_redirect_name),
            302,
            200
        )

    def test_doesnt_create_despesa_when_valor_is_none(self):
        """Verifica se a despesa não é criada quando o valor não é passado para a view"""

        form_data = {
            'nome': 'Despesa 1',
            'valor': ''
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Despesa.objects.exists())

    def test_creates_despesa_when_all_data_is_given(self):
        """Verifica se a despesa é criada quando todos os dados são passados para a view"""

        form_data = {
            'nome': 'Despesa 1',
            'valor': 10.51,
            'vencimento': '2023-07-19'
        }
        self.client.post(self.target_url, data=form_data)

        self.assertTrue(Despesa.objects.exists())
        self.assertEqual(Despesa.objects.last().nome, form_data['nome'])
        self.assertEqual(str(Despesa.objects.last().valor),
                         str(form_data['valor']))

    def test_view_return_form_errors_when_some_data_is_missing(self):
        """Verifica se a view retorna erros de fomrulário quando recebe dados incompletos"""

        form_data = {
            'nome': '',
            'valor': ''
        }
        response = self.client.post(self.target_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'].errors)

    def test_intial_form_is_empty(self):
        """Verifica se a view envia um formulário vazio para o template"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertIsNone(form.initial.get('nome'))
        self.assertIsNone(form.initial.get('valor'))

    def test_form_fields_are_filled_with_previous_values(self):
        """Verifica se a view envia os campos do formulário preenchidos com os valores anteriores em caso de erro de validação"""

        form_data = {
            'nome': 'Despesa 1',
            'valor': '',
        }
        response = self.client.post(self.target_url, data=form_data)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertEqual(
            form['nome'].value(),
            form_data.get('nome')
        )


class EditarDespesaViewTest(TestCase):
    def setUp(self) -> None:
        self.despesa = Despesa.objects.create(
            nome="Despesa 1",
            valor=10.01,
            vencimento='2023-07-19'
        )
        self.expected_template = 'despesa/editar.html'
        self.view_url_name = 'despesa:despesa_editar'
        self.success_redirect_url_name = 'despesa:despesa_listar'
        self.expected_form_type = DespesaForm
        self.client = Client()

    def test_returns_404_when_despesa_doesnt_exist(self):
        """Verifica se a view response com 404 quando a despesa solicitada não existe"""

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
                'pk': self.despesa.id
            }
        ))

        self.assertIsInstance(response.context.get(
            'form'), self.expected_form_type)

    def test_view_uses_expected_template(self):
        """Verifica se a view renderiza o template correto"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_despesa_not_updated_when_no_name_is_given(self):
        """Verifica se a view não atualiza a despesa quando o nome está em branco"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': '',
                'valor': '1.50'
            }
        )
        form_errors = response.context.get('form').errors
        after_request_item = Despesa.objects.get(id=self.despesa.id)

        self.assertEqual(after_request_item, self.despesa)
        self.assertIsNotNone(form_errors)

    def test_despesa_not_updated_when_valor_is_less_than_zero(self):
        """Verifica se a view não atualiza a despesa quando o valor passado é menor que zero"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': self.despesa.nome,
                'periodica': self.despesa.periodica,
                'valor': -0.01,
            }
        )
        form_errors = response.context.get('form').errors
        after_request_item = Despesa.objects.get(id=self.despesa.id)

        self.assertEqual(after_request_item, self.despesa)
        self.assertIsNotNone(form_errors)

    def test_despesa_not_updated_when_valor_is_zero(self):
        """Verifica se a view não atualiza a despesa quando o valor passado é zero"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': self.despesa.nome,
                'valor': 0
            }
        )
        form_errors = response.context.get('form').errors
        after_request_item = Despesa.objects.get(id=self.despesa.id)

        self.assertEqual(after_request_item, self.despesa)
        self.assertIsNotNone(form_errors)

    def test_despesa_updates_when_valor_is_greater_than_zero(self):
        """Verifica se a view atualiza a despesa quando o valor passado é maior que zero"""

        novo_valor = '0.01'
        self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': self.despesa.nome,
                'valor': novo_valor,
                'vencimento': self.despesa.vencimento
            }
        )
        despesa_atualizada = Despesa.objects.get(id=self.despesa.id)

        self.assertEqual(str(despesa_atualizada.valor), novo_valor)

    def test_view_redirects_to_correct_page_after_update(self):
        """Verifica se a view redireciona para a página correta após a atualização da despesa"""

        response = self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': self.despesa.nome,
                'valor': 3,
                'periodica': self.despesa.periodica,
                'vencimento': self.despesa.vencimento
            }
        )

        self.assertRedirects(
            response,
            reverse_lazy(self.success_redirect_url_name),
            302,
            200
        )

    def test_despesa_criada_quando_despesa_periodica_eh_paga(self):
        """Verifica se uma nova despesa é criada quando um despesa que tem periódica como True é editada como paga"""

        quantidade_despesas_antes = Despesa.objects.count()
        self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': self.despesa.id
                }
            ),
            {
                'nome': self.despesa.nome,
                'valor': 3,
                'periodica': True,
                'vencimento': self.despesa.vencimento,
                'paga': True
            }
        )
        quantidade_despesas_depois = Despesa.objects.count()

        self.assertEqual(quantidade_despesas_antes+1,
                         quantidade_despesas_depois)

    def test_despesa_nao_criada_quando_despesa_periodica_paga_eh_salva(self):
        """Verifica se uma nova despesa não é criada quando um despesa periódica já paga é salva novamente"""

        despesa = Despesa.objects.create(
            nome="Despesa 1",
            valor=10.01,
            vencimento='2023-07-19',
            periodica=True,
            paga=True
        )
        quantidade_despesas_antes = Despesa.objects.count()
        self.client.post(
            reverse_lazy(
                self.view_url_name,
                kwargs={
                    'pk': despesa.id
                }
            ),
            {
                'nome': despesa.nome,
                'valor': despesa.valor,
                'periodica': True,
                'vencimento': despesa.vencimento,
                'paga': True
            }
        )
        quantidade_despesas_depois = Despesa.objects.count()

        self.assertEqual(quantidade_despesas_antes,
                         quantidade_despesas_depois)


class RemoverDespesaViewTest(TestCase):
    def setUp(self) -> None:
        self.despesa = Despesa.objects.create(
            nome="Despesa 1",
            valor=10.51,
            vencimento='2023-07-19'
        )
        self.expected_template = 'despesa/remover.html'
        self.client = Client()
        self.view_url_name = 'despesa:despesa_remover'
        self.success_redirect_url_name = 'despesa:despesa_listar'

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_response_is_404_when_despesa_doesnt_exist(self):
        """Verifica se a view retorna 404 quando o atributo 'pk' passado não pertence a nenhuma despesa"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_response_is_400_when_despesa_is_paga(self):
        """Verifica se a view retorna 404 quando o usuário tenta apagar uma despesa já paga"""

        despesa = Despesa.objects.create(
            nome="despesa",
            valor=2.55,
            vencimento='2023-06-30',
            paga=True
        )
        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': despesa.id
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_sends_despesa_to_template(self):
        """Verifica se a view envia ao template a despesa associada ao atributo 'pk' passado na request"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))
        despesa_recebida = response.context.get('despesa')

        self.assertIsNotNone(despesa_recebida)
        self.assertIsInstance(despesa_recebida, Despesa)
        self.assertEqual(self.despesa, despesa_recebida)

    def removes_despesa_on_post_request(self):
        """Verifica se a view realiza a remoção da despesa do banco de dados"""

        initial_count = Despesa.objects.count()
        self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertEqual(initial_count - 1, Despesa.objects.count())

    def test_redirects_to_correct_page_after_delete(self):
        """Verifica se a view redireciona para a página correta após excluir"""

        response = self.client.post(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertRedirects(
            response,
            reverse_lazy(
                self.success_redirect_url_name
            ),
            302,
            200
        )


class RemoverDespesaViewTest(TestCase):
    def setUp(self) -> None:
        self.despesa = Despesa.objects.create(
            nome="Despesa 1",
            valor=10.51
        )
        self.expected_template = 'despesa/remover.html'
        self.client = Client()
        self.view_url_name = 'despesa:despesa_remover'
        self.success_redirect_url_name = 'despesa:despesa_listar'

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_response_is_404_when_despesa_doesnt_exist(self):
        """Verifica se a view retorna 404 quando o atributo 'pk' passado não pertence a nenhuma despesa"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_sends_despesa_to_template(self):
        """Verifica se a view envia ao template a despesa associada ao atributo 'pk' passado na request"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))
        despesa_recebida = response.context.get('despesa')

        self.assertIsNotNone(despesa_recebida)
        self.assertIsInstance(despesa_recebida, Despesa)
        self.assertEqual(self.despesa, despesa_recebida)

    def removes_despesa_on_post_request(self):
        """Verifica se a view realiza a remoção da despesa do banco de dados"""

        initial_count = Despesa.objects.count()
        self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertEqual(initial_count - 1, Despesa.objects.count())

    def test_redirects_to_correct_page_after_delete(self):
        """Verifica se a view redireciona para a página correta após excluir"""

        response = self.client.post(reverse_lazy(
            self.view_url_name,
            kwargs={
                'pk': self.despesa.id
            }
        ))

        self.assertRedirects(
            response,
            reverse_lazy(
                self.success_redirect_url_name
            ),
            302,
            200
        )
