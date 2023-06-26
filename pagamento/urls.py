from django.urls import path
from pagamento.views import home_pagamento_view, pagamento_criar_view

app_name ='pagamento'

urlpatterns = [
    path('', home_pagamento_view, name='home_pagamento'),
    path('criar', pagamento_criar_view, name='pagamento_criar')
]
