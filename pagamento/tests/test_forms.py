from django.test import TestCase
from pagamento.forms import PagamentoForm

class PagamentoFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'titulo': 'Pagamento Teste', 'valor': 100}
        form = PagamentoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'titulo': 'Pagamento Teste'}
        form = PagamentoForm(data=form_data)
        self.assertFalse(form.is_valid())