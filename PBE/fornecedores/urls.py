# fornecedores/urls.py
from django.urls import path
from .views import (
    DashboardView,
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView
)

app_name = 'fornecedores'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produtos/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto-delete'),
]