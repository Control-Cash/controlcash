from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('formas_pagamento/', views.FormaPagamentoListView.as_view(), name='forma_pagamento_lista'),
    path('formas_pagamento/criar/', views.FormaPagamentoCreateView.as_view(), name='forma_pagamento_criar'),
    path('formas_pagamento/<int:pk>/atualizar/', views.FormaPagamentoUpdateView.as_view(), name='forma_pagamento_atualizar'),
    path('formas_pagamento/<int:pk>/remover/', views.FormaPagamentoDeleteView.as_view(), name='forma_pagamento_remover'),

    path('pagamentos/', views.PagamentoListView.as_view(), name='pagamento_lista'),
    path('pagamentos/criar/', views.PagamentoCreateView.as_view(), name='pagamento_criar'),
    path('pagamentos/<int:pk>/atualizar/', views.PagamentoUpdateView.as_view(), name='pagamento_atualizar'),
    path('pagamentos/<int:pk>/remover/', views.PagamentoDeleteView.as_view(), name='pagamento_remover'),
]