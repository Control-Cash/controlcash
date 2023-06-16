from django.test import Client, TestCase
from django.urls import reverse_lazy

from despesa.forms import DespesaForm
from despesa.models import Despesa


class ListarDespesasViewTest(TestCase):
    def setUp(self) -> None:
        self.target_url = reverse_lazy('despesa:despesa_listar')
        self.despesas = [
            Despesa.objects.create(nome="Depesa 1", valor=10.51),
            Despesa.objects.create(nome="Depesa 2", valor=10.52),
            Despesa.objects.create(nome="Depesa 3", valor=10.53),
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
        despesas = response.context.get('despesas')

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
        }
        response = self.client.post(self.target_url, data=form_data)
        despesa_criada = Despesa.objects.last()

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
            'valor': 10.51
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
