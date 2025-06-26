from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produtos')

urlpatterns = [
    path('', include(router.urls)),
]