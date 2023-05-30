from django.urls import path
from pagamento.views import home_pagamento

urlpatterns = [
    path('', home_pagamento, name='home_pagamento'),
]