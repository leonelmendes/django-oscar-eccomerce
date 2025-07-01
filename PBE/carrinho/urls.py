from django.urls import path
from .views import (
    adicionar_ao_carrinho,
    remover_do_carrinho,
    ver_carrinho,
    finalizar_compra,
)

app_name = 'carrinho'

urlpatterns = [
    path('', ver_carrinho, name='ver-carrinho'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover'),
    path('finalizar/', finalizar_compra, name='finalizar-compra'),
]
