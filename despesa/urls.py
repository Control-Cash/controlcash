from django.urls import path

from despesa.views import listar_despesas_view

app_name = 'despesa'

urlpatterns = [
    path('', listar_despesas_view, name='despesa_listar'),
]
