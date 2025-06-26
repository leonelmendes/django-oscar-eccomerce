from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsFornecedorOwnerOrReadOnly

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().select_related('categoria', 'fornecedor')
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsFornecedorOwnerOrReadOnly]

    def perform_create(self, serializer):
        # fornecedor autenticado vira dono do produto
        serializer.save(fornecedor=self.request.user)

    def get_queryset(self):
        # Para PUT/DELETE garantimos via permission; leitura devolve todos
        return super().get_queryset()
    
class ListaCategoriasView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)