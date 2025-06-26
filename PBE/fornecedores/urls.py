# fornecedores/urls.py
from django.urls import path
from .views import (
    FornecedorDashboardView,
    ProdutoFormTemplate,
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
    EncomendaListView,
    EstatisticasView
)

app_name = 'fornecedores'

urlpatterns = [
    path('', FornecedorDashboardView.as_view(), name='dashboard'),
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    #path('produtos/novo/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/adicionar/', ProdutoFormTemplate.as_view(), name='produto-add'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produtos/<int:pk>/remover/', ProdutoDeleteView.as_view(), name='produto-delete'),
    path('encomendas/', EncomendaListView.as_view(), name='encomenda-list'),
    path('estatisticas/', EstatisticasView.as_view(), name='estatisticas'),
    path('dashboard/', FornecedorDashboardView.as_view(), name='dashboard'),
]