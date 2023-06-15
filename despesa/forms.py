from django import forms

from despesa.models import Despesa


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'periodica']
        help_texts = {
            'periodica': "Marque caso essa despesa seja recorrente"
        }
