from django.forms import ModelForm
from .models import Produto

class CadastrarProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
