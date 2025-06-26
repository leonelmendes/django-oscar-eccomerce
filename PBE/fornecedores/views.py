# fornecedores/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from produtos.models import Produto
from users.models import FornecedorProfile
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from .models import Encomenda
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from produtos.models import Categoria

def fornecedor_required(user):
    return user.is_authenticated and hasattr(user, 'fornecedorprofile')

class FornecedorRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(fornecedor_required))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class FornecedorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'oscar/dashboard/fornecedores/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione dados básicos para evitar erros no template
        context['produtos_count'] = 0
        context['encomendas_count'] = 0
        context['total_vendas'] = 0
        return context

class ProdutoListView(LoginRequiredMixin, FornecedorRequiredMixin, ListView):
    model = Produto
    template_name = 'fornecedores/produto_list.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)

class ProdutoCreateView(LoginRequiredMixin, FornecedorRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'unidade_venda', 'quantidade', 'imagem']
    template_name = 'fornecedores/produto_form.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def form_valid(self, form):
        form.instance.fornecedor = self.request.user
        return super().form_valid(form)

class ProdutoUpdateView(LoginRequiredMixin, FornecedorRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'unidade_venda', 'quantidade', 'imagem']
    template_name = 'fornecedores/produto_edit.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)

class ProdutoDeleteView(LoginRequiredMixin, FornecedorRequiredMixin, DeleteView):
    model = Produto
    template_name = 'fornecedores/produto_confirm_delete.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)
    
class EncomendaListView(LoginRequiredMixin, FornecedorRequiredMixin, ListView):
    model = Encomenda
    template_name = 'oscar/dashboard/fornecedores/encomenda_list.html'
    context_object_name = 'encomendas'
    paginate_by = 10
    
    def get_queryset(self):
        return Encomenda.objects.filter(
            fornecedor=self.request.user
        ).select_related('cliente').order_by('-data_criacao')

class EstatisticasView(LoginRequiredMixin, FornecedorRequiredMixin, TemplateView):
    template_name = 'oscar/dashboard/fornecedores/estatisticas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Estatísticas básicas
        encomendas = Encomenda.objects.filter(fornecedor=user)
        
        # Total de vendas
        total_vendas = encomendas.aggregate(
            total=Sum('total')
        )['total'] or 0
        
        # Vendas dos últimos 30 dias
        data_limite = timezone.now() - timedelta(days=30)
        vendas_30dias = encomendas.filter(
            data_criacao__gte=data_limite
        ).count()
        
        # Produtos mais vendidos (ajuste conforme seu modelo)
        # produtos_mais_vendidos = ...
        
        context.update({
            'total_vendas': total_vendas,
            'vendas_30dias': vendas_30dias,
            'total_encomendas': encomendas.count(),
            # Adicione mais dados conforme necessário
        })
        
        return context
    
class ProdutoFormTemplate(LoginRequiredMixin, FornecedorRequiredMixin, TemplateView):
    template_name = 'fornecedores/produto_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from produtos.models import Categoria
        context["categorias"] = Categoria.objects.all()
        return context