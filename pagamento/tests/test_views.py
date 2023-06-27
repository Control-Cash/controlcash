from django.test import TestCase
from django.urls import reverse
from pagamento.models import Pagamento
# Create your tests here.

class PagamentoViewListarPagamento(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_pagamentos = 10


        for pagamento_id in range(num_pagamentos):
            Pagamento.objects.create(
                valor_pagamento=pagamento_id,
                data=pagamento_id,
            )
        
    def test_view_url_exists_at_desired_location(self):
        reposta = self.client.get('/pagamento/')
        self.assertEqual(reposta.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resposta = self.client.get(reverse('home_pagamento'))
        self.assertEqual(resposta.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home_pagamento'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_pagamento.html')