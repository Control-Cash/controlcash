from django import forms
from .models import FormaPagamento, Pagamento

""" class FormaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = '__all__' """

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'