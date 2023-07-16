from django import forms

from despesa.models import Despesa


class DateInput(forms.DateInput):
    input_type = 'date'


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'vencimento', 'periodica', 'paga']
        widgets = {
            'vencimento': DateInput(),
            'valor': forms.NumberInput(attrs={'min': '0.01'})
        }
        help_texts = {
            'periodica': "Marque caso essa despesa seja recorrente"
        }
