from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ClienteProfile, FornecedorProfile


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class ClienteRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClienteProfile
        fields = ('user', 'telefone')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user.tipo = 'cliente' 
        user.save()
        cliente = ClienteProfile.objects.create(user=user, **validated_data)
        return cliente

class FornecedorRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FornecedorProfile
        fields = ('user', 'empresa', 'telefone')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user.is_staff = True
        user.save() 
        fornecedor = FornecedorProfile.objects.create(user=user, **validated_data)
        return fornecedor