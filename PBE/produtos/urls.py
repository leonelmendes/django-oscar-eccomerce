from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos.views import ListaCategoriasView, ProdutoViewSet


router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produtos')
#router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('', include(router.urls)),
     path('categorias/', ListaCategoriasView.as_view(), name='categorias-lista'),
]