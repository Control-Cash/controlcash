from django.urls import path
from produto.views import home, viewCriarProduto, viewEditarProduto, viewAtualizarProduto, viewVizualizarProduto, viewDeletarProduto

urlpatterns = [
    path('', home, name='homeProduto'),
    path('criar/', viewCriarProduto, name='criarProduto'),
    path('vizualizar/<int:id>', viewVizualizarProduto, name='vizualizarProduto'),
    path('editar/<int:id>', viewEditarProduto, name='editarProduto'),
    path('update/<int:id>', viewAtualizarProduto, name='atualizarProduto'),
    path('deletar/<int:id>', viewDeletarProduto, name='deletarProduto'),
]