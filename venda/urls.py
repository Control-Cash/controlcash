from django.urls import path

from venda.views import criar_venda_view, listar_vendas_view

urlpatterns = [
    path('', listar_vendas_view, name='venda_listar'),
]
