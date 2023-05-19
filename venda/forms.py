from django import forms

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


class ClienteForm(forms.ModelForm):
    class Meta:
        fields = ['nome', 'email']
        model = Cliente
