from http import client
from django.test import Client, TestCase
from django.urls import reverse_lazy

from fornecedor.forms import CadastrarFornecedor
from fornecedor.models import Fornecedor
from venda.forms import EnderecoForm
from venda.models import Endereco


class CriarFornecedorViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.target_url = reverse_lazy('fornecedor_criar')
        self.endereco = Endereco.objects.create(
            cep='12345678',
            numero=10,
            rua='Rua Exemplo',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='Estado Exemplo',
            pais='Brasil',
            complemento='Complemento Exemplo'
        )
        self.form_data = {
            'nome': 'Havaianas',
            'email': 'havaianas@chinelo.com',
            'cep': '12345678',
            'numero': 10,
            'rua': 'Rua Exemplo',
            'bairro': 'Bairro Exemplo',
            'cidade': 'Cidade Exemplo',
            'estado': 'Estado Exemplo',
            'pais': 'Brasil',
            'complemento': 'Complemento Exemplo'

        }
        self.expected_template = 'formCriarForcedor.html'
        self.fornecedor = Fornecedor.objects.create(
            nome=self.form_data.get('nome'),
            email=self.form_data.get('email'),
            endereco=self.endereco
        )

    def test_view_sends_form_to_template(self):
        """Verifica se a view envia o formulário ao template"""

        response = self.client.get(self.target_url)
        self.assertIsNotNone(
            response.context.get('form'),
            "'form' não é enviado pela view")

    def test_form_sended_to_template_is_fornecedor_form(self):
        """Verifica se a view envia o formulário correto ao template"""

        response = self.client.get(self.target_url)

        self.assertIsInstance(
            response.context.get('form'),
            CadastrarFornecedor,
            "'form' enviado pela view não é o esperado")
        self.assertIsInstance(
            response.context.get('endereco_form'),
            EnderecoForm,
            "'endereco_form' enviado pela view não é o esperado")

    def test_empty_form_doesnt_save(self):
        """Verifica se a view não cria um fornecedor quando um post request tem os dados em branco"""

        fornecedor_count = Fornecedor.objects.count()
        self.client.post(self.target_url, {
            'email': 'havaianas@chinelo.com',
            'cep': '12345678',
            'numero': 10,
            'rua': 'Rua Exemplo',
            'bairro': 'Bairro Exemplo',
            'cidade': 'Cidade Exemplo',
            'estado': 'Estado Exemplo',
            'pais': 'Brasil',
            'complemento': 'Complemento Exemplo'
        })

        self.assertEqual(
            fornecedor_count,
            Fornecedor.objects.count(),
            "Um fornecedor foi criado com o formulário em branco"
        )

    def test_empty_form_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe dados em branco"""

        response = self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': '',
                'cep': '',
                'numero': '',
                'rua': '',
                'bairro': '',
                'cidade': '',
                'estado': '',
                'pais': '',
                'complemento': ''
            }
        )
        form = response.context.get('form')

        self.assertIsNotNone(form.errors)

    def test_filled_form_saves(self):
        """Verifica se a view cria um fornecedor quando um post request tem os dados corretos"""

        fornecedor_count = Fornecedor.objects.count()
        self.client.post(self.target_url, self.form_data)

        self.assertEqual(
            fornecedor_count + 1,
            Fornecedor.objects.count(),
            "Um fornecedor não foi criado com o formulário preechido")

    def test_empty_required_fields_doesnt_save(self):
        """Verifica se a view nao cria um fornecedor quando um post request tem os dados obrigatótios em branco"""

        fornecedor_count = Fornecedor.objects.count()
        self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': 'havaianas@chinelo.com',
                'cep': '12345678',
                'numero': 10,
                'rua': 'Rua Exemplo',
                'bairro': 'Bairro Exemplo',
                'cidade': 'Cidade Exemplo',
                'estado': 'Estado Exemplo',
                'pais': 'Brasil',
                'complemento': 'Complemento Exemplo'
            }
        )

        self.assertEqual(
            fornecedor_count,
            Fornecedor.objects.count(),
            "Um fornecedor foi criado com os campos obrigatŕios do formulário em branco")

    def test_empty_optional_fields_saves(self):
        """Verifica se a view cria um fornecedor quando um post request tem os dados opcionais em branco"""

        fornecedor_count = Fornecedor.objects.count()
        self.client.post(
            self.target_url,
            {
                'nome': self.form_data.get('nome'),
                'email': self.form_data.get('email'),
                'bairro': self.form_data.get('bairro'),
                'cidade': self.form_data.get('cidade'),
                'pais': self.form_data.get('pais'),
                'numero': self.form_data.get('numero'),
                'cep': self.form_data.get('cep'),
                'rua': self.form_data.get('rua'),
                'complemento': '',
                'estado': self.form_data.get('estado')
            }
        )

        self.assertEqual(
            fornecedor_count + 1,
            Fornecedor.objects.count(),
            "Um fornecedor não foi criado com os campos opcionais do formulário em branco"
        )

    def test_empty_required_fields_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe todos os dados obrigatórios em branco"""

        response = self.client.post(
            self.target_url,
            {
                'nome': '',
                'email': '',
                'cep': '',
                'numero': '',
                'rua': '',
                'bairro': '',
                'cidade': '',
                'estado': '',
                'pais': '',
                'complemento': 'Complemento Exemplo'
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
        """Verifica se a view redireciona quando uma solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)

        self.assertEqual(
            response.status_code,
            302,
            'A view não redirecionou após post request bem sucedido'
        )

    def test_successful_post_request_redirects_to_expected_url(self):
        """Verifica se a view redireciona para a url correta quando uma solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)

        self.assertRedirects(
            response,
            reverse_lazy(
                'fornecedor_listar',
            ),
            302,
            200
        )


class ListarFornecedoresViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.target_url = reverse_lazy('fornecedor_listar')
        self.fornecedores_data = [
            {
                'nome': 'Havaianas',
                'email': 'havaianas@chinelo.com',
                'cep': '12345678',
                'numero': 10,
                'rua': 'Rua Exemplo',
                'bairro': 'Bairro Exemplo',
                'cidade': 'Cidade Exemplo',
                'estado': 'Estado Exemplo',
                'pais': 'Brasil',
                'complemento': 'Complemento Exemplo'
            },
            {
                'nome': 'Magalu',
                'email': 'magalu@gmail.com',
                'cep': '12345678',
                'numero': 10,
                'rua': 'Rua Exemplo',
                'bairro': 'Bairro Exemplo',
                'cidade': 'Cidade Exemplo',
                'estado': 'Estado Exemplo',
                'pais': 'Brasil',
                'complemento': 'Complemento Exemplo'
            },
            {
                'nome': 'Americanas',
                'email': 'americanas@varejo.com',
                'cep': '12345678',
                'numero': 10,
                'rua': 'Rua Exemplo',
                'bairro': 'Bairro Exemplo',
                'cidade': 'Cidade Exemplo',
                'estado': 'Estado Exemplo',
                'pais': 'Brasil',
                'complemento': 'Complemento Exemplo'
            },
        ]
        self.endereco = Endereco.objects.create(
            cep='12345678',
            numero=10,
            rua='Rua Exemplo',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='Estado Exemplo',
            pais='Brasil',
            complemento='Complemento Exemplo'
        )
        self.expected_template = 'homeFornecedores.html'

    def test_view_sends_page_obj_to_template(self):
        """Verifica se a view envia uma variavel 'page_obj' ao template"""

        response = self.client.get(self.target_url)

        self.assertIsNotNone(
            response.context.get('page_obj'),
            "'page_obj' não é enviado pela view"
        )

    def test_fornecedores_sended_to_template_contains_fornecedores_data(self):
        """Verifica se a view envia os dados dos fornecedores ao template"""

        Fornecedor.objects.create(
            nome=self.fornecedores_data[0].get('nome'),
            email=self.fornecedores_data[0].get('email'),
            endereco=self.endereco,
        )

        response = self.client.get(self.target_url)
        fornecedores = response.context.get('page_obj').object_list

        self.assertTrue(
            all(isinstance(fornecedor, Fornecedor)
                for fornecedor in fornecedores),
            "Os objetos retornados não são do modelo 'Fornecedor'"
        )

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )

    def test_all_fornecedores_are_sended_to_template(self):
        """Verifica se a view envia todos os fornecedores ao template"""

        fornecedor1 = Fornecedor.objects.create(
            nome=self.fornecedores_data[0].get('nome'),
            email=self.fornecedores_data[0].get('email'),
            endereco=self.endereco,
        )
        fornecedor2 = Fornecedor.objects.create(
            nome=self.fornecedores_data[1].get('nome'),
            email=self.fornecedores_data[1].get('email'),
            endereco=self.endereco,
        )
        fornecedor3 = Fornecedor.objects.create(
            nome=self.fornecedores_data[2].get('nome'),
            email=self.fornecedores_data[2].get('email'),
            endereco=self.endereco,
        )

        response = self.client.get(self.target_url)
        fornecedores = response.context.get('page_obj').object_list

        self.assertIn(fornecedor1, fornecedores)
        self.assertIn(fornecedor2, fornecedores)
        self.assertIn(fornecedor3, fornecedores)

    def test_search_returns_only_matching_objects(self):
        """Verifica de a busca retorna apenas os objetos que correspondem"""

        Fornecedor.objects.create(
            nome=self.fornecedores_data[0].get('nome'),
            email=self.fornecedores_data[0].get('email'),
            endereco=self.endereco,
        )
        Fornecedor.objects.create(
            nome=self.fornecedores_data[1].get('nome'),
            email=self.fornecedores_data[1].get('email'),
            endereco=self.endereco,
        )
        Fornecedor.objects.create(
            nome=self.fornecedores_data[2].get('nome'),
            email=self.fornecedores_data[2].get('email'),
            endereco=self.endereco,
        )

        response = self.client.get(f"{self.target_url}?fornecedor=ame")
        fornecedores = response.context.get('page_obj').object_list

        self.assertEqual(len(fornecedores), 1)


class DetalharFornecedorViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.expected_template = 'vizualizarFornecedor.html'
        self.endereco = Endereco.objects.create(
            cep='12345678',
            numero=10,
            rua='Rua Exemplo',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='Estado Exemplo',
            pais='Brasil',
            complemento='Complemento Exemplo'
        )
        self.fornecedor_criado = Fornecedor.objects.create(
            nome='Americanas',
            email='americanas@varejo.com',
            endereco=self.endereco,
        )

    def test_view_returns_fornecedor_requested(self):
        """Veriica se a view retorna ao template o fornecedor solicitado"""

        response = self.client.get(
            reverse_lazy(
                'fornecedor_vizualizar',
                kwargs={
                    'id': self.fornecedor_criado.id
                }
            )
        )
        fornecedor_retornado = response.context.get('fornecedor')

        self.assertIsNotNone(
            fornecedor_retornado,
            "A view não retorna a variável 'fornecedor'"
        )
        self.assertEqual(
            self.fornecedor_criado,
            fornecedor_retornado,
            "A view não retornou o fornecedor solicitado"
        )

    def test_view_returns_404_when_fornecedor_is_unknown(self):
        """Verifica se a view retorna uma resposta 404 quando o fornecedor solicitado não existe"""

        response = self.client.get(
            reverse_lazy(
                'fornecedor_vizualizar',
                kwargs={
                    'id': 50
                }
            )
        )

        self.assertIsNone(response.context.get('fornecedor'))
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(
            reverse_lazy(
                'fornecedor_vizualizar',
                kwargs={
                    'id': self.fornecedor_criado.id
                }
            )
        )

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )
