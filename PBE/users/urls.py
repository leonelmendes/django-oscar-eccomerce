from django.urls import path
from .views import ClienteRegisterView, FornecedorRegisterView

urlpatterns = [
    path('register/cliente/', ClienteRegisterView.as_view(), name='register-cliente'),
    path('register/fornecedor/', FornecedorRegisterView.as_view(), name='register-fornecedor'),
]