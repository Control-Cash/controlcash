from django.urls import path

from venda.views import (criar_venda_view, desativar_venda_view,
                         detalhar_venda_view, editar_quatidade_item_view,
                         finalizar_venda_view, listar_vendas_view, reativar_venda_view,
                         remover_item_view)

urlpatterns = [
    path('', listar_vendas_view, name='venda_listar'),
    path('criar', criar_venda_view, name='venda_criar'),
    path('<int:pk>', detalhar_venda_view, name='venda_detalhar'),
    path('<int:pk>/desativar', desativar_venda_view, name='venda_desativar'),
    path('<int:pk>/finalizar', finalizar_venda_view, name='venda_finalizar'),
    path('<int:pk>/reativar', reativar_venda_view, name='venda_reativar'),
    path('itens/<int:pk>/editar', editar_quatidade_item_view, name='item_editar'),
    path('itens/<int:pk>/remover', remover_item_view, name='item_remover'),
]
