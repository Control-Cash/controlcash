from django.forms import ModelForm
from .models import Fornecedor

class CadastrarFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','email']