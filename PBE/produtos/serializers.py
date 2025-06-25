from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Produto, Categoria

User = get_user_model()

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), write_only=True, source='categoria'
    )
    fornecedor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'imagem', 'preco',
            'unidade_venda','quantidade', 'categoria', 'categoria_id', 'fornecedor'
        ]