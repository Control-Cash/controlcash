from django.urls import path
from produto.views import home_produto, view_criar_produto, view_editar_produto, view_atualizar_produto, view_vizualizar_produto, view_deletar_produto

urlpatterns = [
    path('', home_produto, name='homeProduto'),
    path('criar/', view_criar_produto, name='criarProduto'),
    path('vizualizar/<int:id>', view_vizualizar_produto, name='vizualizarProduto'),
    path('update/<int:id>', view_atualizar_produto, name='atualizarProduto'),
    path('deletar/<int:id>', view_deletar_produto, name='deletarProduto'),
]