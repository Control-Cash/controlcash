from django.test import TestCase
from django.urls import reverse
from pagamento.models import Pagamento

class PagamentoViewTestCase(TestCase):
    def setUp(self):
        self.pagamento1 = Pagamento.objects.create(valor=100.00, data='2023-07-11', status='pendente', id_cliente=1)
        self.pagamento2 = Pagamento.objects.create(valor=200.00, data='2023-07-12', status='recebido', id_cliente=2)

    def test_home_pagamento_view(self):
        response = self.client.get(reverse('pagamento:home_pagamento'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_pagamento.html')
        self.assertContains(response, '100')
        self.assertContains(response, '200')

    def test_criar_pagamento_view(self):
        response = self.client.get(reverse('pagamento:pagamento_criar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criar_pagamento.html')

        response = self.client.post(reverse('pagamento:pagamento_criar'), {'valor': 300.00, 'data': '2023-07-13', 'status': 'pendente', 'id_cliente': 3})
        self.assertRedirects(response, reverse('pagamento:home_pagamento'))
        self.assertEqual(Pagamento.objects.count(), 3)

    def test_editar_pagamento_view(self):
        response = self.client.get(reverse('pagamento:pagamento_editar', args=[self.pagamento1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_pagamento.html')

        response = self.client.post(reverse('pagamento:pagamento_editar', args=[self.pagamento1.id]), {'valor': 400.00, 'data': '2023-07-14', 'status': 'recebido', 'id_cliente': 1})
        self.assertRedirects(response, reverse('pagamento:home_pagamento'))
        self.pagamento1.refresh_from_db()
        self.assertEqual(self.pagamento1.valor, 400.00)

    def test_remover_pagamento_view(self):
        response = self.client.get(reverse('pagamento:pagamento_remover', args=[self.pagamento1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'remover_pagamento.html')

        response = self.client.post(reverse('pagamento:pagamento_remover', args=[self.pagamento1.id]))
        self.assertRedirects(response, reverse('pagamento:home_pagamento'))
        self.assertEqual(Pagamento.objects.count(), 1)

