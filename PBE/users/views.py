from django.shortcuts import render
from rest_framework import generics
from .models import ClienteProfile, FornecedorProfile
from .serializers import ClienteRegisterSerializer, FornecedorRegisterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class ClienteRegisterView(generics.CreateAPIView):
    queryset = ClienteProfile.objects.all()
    serializer_class = ClienteRegisterSerializer

class FornecedorRegisterView(generics.CreateAPIView):
    queryset = FornecedorProfile.objects.all()
    serializer_class = FornecedorRegisterSerializer