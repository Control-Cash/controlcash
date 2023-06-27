from django.test import TestCase, Client
from django.urls import reverse
from pagamento.models import Pagamento
from pagamento.forms import PagamentoForm

class PagamentoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home_pagamento_view')
        self.create_url = reverse('criar_pagamento_view')
        self.edit_url = reverse('editar_pagamento_view', args=[1])  # Supondo que o ID do pagamento seja 1
        self.remove_url = reverse('remover_pagamento_view', args=[1])  # Supondo que o ID do pagamento seja 1

    def test_home_pagamento_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_pagamento.html')

    def test_criar_pagamento_view(self):
        form_data = {'titulo': 'Pagamento Teste', 'valor': 100}
        response = self.client.post(self.create_url, data=form_data)
        self.assertEqual(response.status_code, 302)  # Verifica se houve redirecionamento após o POST
        self.assertEqual(response.url, '/pagamento')

    def test_editar_pagamento_view(self):
        pagamento = Pagamento.objects.create(titulo='Pagamento Teste', valor=100)
        form_data = {'titulo': 'Pagamento Editado', 'valor': 200}
        response = self.client.post(self.edit_url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/pagamento')

    def test_remover_pagamento_view(self):
        pagamento = Pagamento.objects.create(titulo='Pagamento Teste', valor=100)
        response = self.client.post(self.remove_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/pagamento')
