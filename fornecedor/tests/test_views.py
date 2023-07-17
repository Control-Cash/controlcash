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


class EditarFornecedorViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.expected_template = 'formAtualizaFornecedor.html'
        self.endereco_criado = Endereco.objects.create(
            rua='Rua do limoeiro',
            bairro='Centro',
            cidade='Sao Paulo',
            estado='SP',
            pais='Brasil',
            cep='01001000',
            numero=123,
            complemento=''
        )
        self.fornecedor_criado = Fornecedor.objects.create(
            nome='Americanas',
            email='americanas@gmail.com',
            endereco=self.endereco_criado
        )
        self.form_data = {
            'nome': 'Magalu',
            'email': 'magalu@outlook.com',
            'rua': 'Rua do limoeiro',
            'bairro': 'Centro',
            'cidade': 'Sao Paulo',
            'estado': 'SP',
            'pais': 'Brasil',
            'cep': '01001000',
            'numero': '321',
            'complemento': '',
        }
        self.target_url = reverse_lazy(
            'fornecedor_atualizar',
            kwargs={
                'id': self.fornecedor_criado.id
            }
        )

    def test_view_sends_form_to_template(self):
        """Verifica se a view envia o formulário ao template"""

        response = self.client.get(self.target_url)

        self.assertIsNotNone(
            response.context.get('form'),
            "'form' não é enviado pela view"
        )

    def test_form_sended_to_template_is_correct_form(self):
        """Verifica se a view envia o formulário correto ao template"""

        response = self.client.get(self.target_url)

        self.assertIsInstance(
            response.context.get('form'),
            CadastrarFornecedor,
            "'form' enviado pela view não é o correto"
        )
        self.assertIsInstance(
            response.context.get('endereco_form'),
            EnderecoForm,
            "'endereco_form' enviado pela view não é o correto"
        )

    def test_empty_form_doesnt_save(self):
        """Verifica se a view não salva os dados quando um post request tem os dados em branco"""

        self.client.post(self.target_url, {
            'nome': '',
            'email': '',
            'rua': '',
            'bairro': '',
            'cidade': '',
            'estado': '',
            'pais': '',
            'cep': '',
            'numero': '',
            'complemento': '',
        })
        fornecedor_atualizado = Fornecedor.objects.get(
            id=self.fornecedor_criado.id)

        self.assertEqual(
            fornecedor_atualizado.nome,
            self.fornecedor_criado.nome,
            "O nome do fornecedor foi alterado com o formulário em branco"
        )
        self.assertEqual(
            fornecedor_atualizado.email,
            self.fornecedor_criado.email,
            "O email do fornecedor foi alterado com o formulário em branco"
        )

    def test_filled_form_saves(self):
        """Verifica se a view salva os dados quando um post request tem os dados corretos"""

        self.client.post(self.target_url, self.form_data)
        self.fornecedor_criado.refresh_from_db()

        self.assertEqual(
            self.fornecedor_criado.nome,
            self.form_data.get('nome'),
            "O nome do fornecedor não foi alterado com o formulário preenchido corretamente"
        )
        self.assertEqual(
            self.fornecedor_criado.email,
            self.form_data.get('email'),
            "O email do fornecedor não foi alterado com o formulário preenchido corretamente"
        )

        self.assertEqual(
            str(self.fornecedor_criado.endereco.numero),
            self.form_data.get('numero'),
            "O endereço do fornecedor não foi alterado com o formulário preenchido corretamente"
        )

    def test_view_uses_correct_template(self):
        """Verifica se a view usa o template correto na renderização"""

        response = self.client.get(self.target_url)

        self.assertTemplateUsed(
            response,
            self.expected_template,
            'A view usou um template diferente do esperado'
        )

    def test_view_returns_404_when_fornecedor_is_unknown(self):
        """Verifica se a view retorna uma resposta 404 quando o fornecedor solicitado não existe"""

        response = self.client.get(
            reverse_lazy(
                'fornecedor_atualizar',
                kwargs={
                    'id': 50
                }
            )
        )

        self.assertIsNone(response.context.get('form'))
        self.assertEqual(response.status_code, 404)

    def test_empty_required_fields_doesnt_save(self):
        """Verifica se a view nao atualiza um fornecedor quando um post request tem os dados obrigatótios em branco"""

        self.client.post(self.target_url, {
            'nome': '',
            'email': '',
            'rua': 'Rua do limoeiro',
            'bairro': 'Centro',
            'cidade': '',
            'estado': 'SP',
            'pais': 'Brasil',
            'cep': '01001000',
            'numero': '321',
            'complemento': '',
        })
        fornecedor_atualizado = Fornecedor.objects.get(
            id=self.fornecedor_criado.id)

        self.assertEqual(
            fornecedor_atualizado.nome,
            self.fornecedor_criado.nome,
            "O fornecedor foi atualizado com os campos obrigatŕios do formulário em branco"
        )

    def test_empty_optional_fields_saves(self):
        """Verifica se a view atualiza um fornecedor quando um post request tem os dados opcionais em branco"""

        self.client.post(self.target_url, {
            'nome': self.form_data.get('nome'),
            'email': self.form_data.get('email'),
            'rua': self.form_data.get('rua'),
            'bairro': self.form_data.get('bairro'),
            'cidade': self.form_data.get('cidade'),
            'estado': self.form_data.get('estado'),
            'pais': self.form_data.get('pais'),
            'numero': self.form_data.get('numero'),
            'cep': self.form_data.get('cep'),
            'complemento': '',
        }
        )
        fornecedor_atualizado = Fornecedor.objects.get(
            id=self.fornecedor_criado.id)

        self.assertEqual(
            fornecedor_atualizado.nome,
            self.form_data.get('nome'),
            "Um fornecedor não foi atualizado com os campos opcionais do formulário em branco"
        )

    def test_empty_required_fields_return_errors(self):
        """Verifica se a view envia erros ao template quando recebe todos os dados obrigatórios em branco"""

        response = self.client.post(self.target_url, {
            'nome': '',
            'email': '',
            'rua': '',
            'bairro': '',
            'cidade': '',
            'estado': '',
            'pais': '',
            'cep': '',
            'numero': '',
            'complemento': 'lateral',
        })
        form = response.context.get('form')

        self.assertIsNotNone(form.errors)

    def test_redirects_to_correct_page_on_update(self):
        """Verifica se a view redireciona para a url correta quando uma solicitação post é enviada corretamente com todos os dados"""

        response = self.client.post(self.target_url, self.form_data)

        self.assertRedirects(
            response,
            reverse_lazy('fornecedor_listar'),
            302,
            200
        )

    def test_form_loads_with_values_from_model(self):
        """Verifica se a view envia o formulário com os campos preenchidos com os valores atuais salvos no banco de dados para o template"""

        response = self.client.get(self.target_url)
        form = response.context.get('form')

        self.assertIsNotNone(form)
        self.assertEqual(form.initial.get('nome'), self.fornecedor_criado.nome)
        self.assertEqual(form.initial.get('email'),
                         self.fornecedor_criado.email)


class RemoverFornecedorViewTest(TestCase):
    def setUp(self) -> None:
        self.endereco_criado = Endereco.objects.create(
            rua='Rua do limoeiro',
            bairro='Centro',
            cidade='Sao Paulo',
            estado='SP',
            pais='Brasil',
            cep='01001000',
            numero=123,
            complemento=''
        )
        self.fornecedor = Fornecedor.objects.create(
            nome='João',
            email="joao@gmail.com",
            endereco=self.endereco_criado,
        )
        self.expected_template = 'excluir_fornecedor.html'
        self.client = Client()
        self.view_url_name = 'fornecedor_deletar'
        self.success_redirect_url_name = 'fornecedor_listar'

    def test_renders_correct_template(self):
        """Verifica se a view renderiza o template esperado"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'id': self.fornecedor.id
            }
        ))

        self.assertTemplateUsed(response, self.expected_template)

    def test_response_is_404_when_fornecedor_doesnt_exist(self):
        """Verifica se a view retorna 404 quando o atributo 'id' passado não pertence a nenhum fornecedor"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'id': 8000
            }
        ))

        self.assertEqual(response.status_code, 404)

    def test_view_sends_fornecedor_to_template(self):
        """Verifica se a view envia ao template o fornecedor associado ao atributo 'id' passado na request"""

        response = self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'id': self.fornecedor.id
            }
        ))
        fornecedor_recebido = response.context.get('fornecedor')

        self.assertIsNotNone(fornecedor_recebido)
        self.assertIsInstance(fornecedor_recebido, Fornecedor)
        self.assertEqual(self.fornecedor, fornecedor_recebido)

    def removes_fornecedor_on_post_request(self):
        """Verifica se a view realiza a remoção do fornecedor do banco de dados"""

        initial_count = Fornecedor.objects.count()
        self.client.get(reverse_lazy(
            self.view_url_name,
            kwargs={
                'id': self.fornecedor.id
            }
        ))

        self.assertEqual(initial_count - 1, Fornecedor.objects.count())

    def test_redirects_to_correct_page_after_delete(self):
        """Verifica se a view redireciona para a página correta após excluir"""

        response = self.client.post(reverse_lazy(
            self.view_url_name,
            kwargs={
                'id': self.fornecedor.id
            }
        ))

        self.assertRedirects(
            response,
            reverse_lazy(self.success_redirect_url_name),
            302,
            200
        )
