from django.test import TestCase
from pagamento.models import Pagamento

class PagamentoModelTest(TestCase):
    def test_create_pagamento(self):
        pagamento = Pagamento.objects.create(titulo='Pagamento Teste', valor=100)
        self.assertEqual(pagamento.titulo, 'Pagamento Teste')
        self.assertEqual(pagamento.valor, 100)