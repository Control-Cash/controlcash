from django.urls import path
from pagamento.views import home_pagamento_view, criar_pagamento_view, editar_pagamento_view, remover_pagamento_view

app_name ='pagamento'

urlpatterns = [
    path('', home_pagamento_view, name='home_pagamento'),
    path('criar', criar_pagamento_view, name='pagamento_criar'),
    path('editar/<int:pk>', editar_pagamento_view, name='pagamento_editar'),
    path('remover/<int:pk>', remover_pagamento_view, name='pagamento_remover'),
]
