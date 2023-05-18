from django import forms

from venda.models import Venda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = []
