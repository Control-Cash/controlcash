from django.urls import path

from despesa.views import (criar_despesa_view, editar_despesa_view,
                           listar_despesas_view, remover_despesa_view)

app_name = 'despesa'

urlpatterns = [
    path('', listar_despesas_view, name='despesa_listar'),
    path('criar', criar_despesa_view, name='despesa_criar'),
    path('editar/<int:pk>', editar_despesa_view, name='despesa_editar'),
    path('remover/<int:pk>', remover_despesa_view, name='despesa_remover'),
]
