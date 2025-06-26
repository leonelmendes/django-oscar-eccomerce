from django.urls import path
from produtos.models import Produto, Categoria
from .views import CustomCatalogueView

app_name = 'catalogue_override'

urlpatterns = [
    path('', CustomCatalogueView.as_view(), name='product-list'),
    path('', CustomCatalogueView.as_view(), name='browse'),
]
