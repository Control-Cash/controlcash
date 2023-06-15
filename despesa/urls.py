from django.urls import path

from despesa.views import criar_despesa_view, listar_despesas_view

app_name = 'despesa'

urlpatterns = [
    path('', listar_despesas_view, name='despesa_listar'),
    path('criar', criar_despesa_view, name='despesa_criar'),
]
