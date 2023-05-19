from django import forms

from produto.models import Produto
from venda.models import Cliente, Item


class CriarVendaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(Cliente.objects.all())

    class Meta:
        model = Item
        fields = ['produto', 'quantidade']


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['produto', 'quantidade']


class EditarItemVendaForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantidade']
