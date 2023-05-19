from django import forms

from venda.models import Item


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['produto', 'quantidade']


class EditarItemVendaForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantidade']
