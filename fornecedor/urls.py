from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_fornecedores, name='fornecedor_listar'),
    path('criar/', cadastrar_fornecedor, name='fornecedor_criar'),
    path('atualizar/<int:id>', atualizar_fornecedor, name='fornecedor_atualizar'),
]