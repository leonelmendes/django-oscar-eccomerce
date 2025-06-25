# fornecedores/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from produtos.models import Produto
from users.models import FornecedorProfile

class FornecedorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'fornecedorprofile')

class DashboardView(LoginRequiredMixin, FornecedorRequiredMixin, TemplateView):
    template_name = 'fornecedores/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fornecedor = self.request.user.fornecedorprofile
        context['produtos_count'] = Produto.objects.filter(fornecedor=self.request.user).count()
        context['empresa'] = fornecedor.empresa
        return context

class ProdutoListView(LoginRequiredMixin, FornecedorRequiredMixin, ListView):
    model = Produto
    template_name = 'fornecedores/produto_list.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)

class ProdutoCreateView(LoginRequiredMixin, FornecedorRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'unidade_medida', 'estoque', 'imagem']
    template_name = 'fornecedores/produto_form.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def form_valid(self, form):
        form.instance.fornecedor = self.request.user
        return super().form_valid(form)

class ProdutoUpdateView(LoginRequiredMixin, FornecedorRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'unidade_medida', 'estoque', 'imagem']
    template_name = 'fornecedores/produto_form.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)

class ProdutoDeleteView(LoginRequiredMixin, FornecedorRequiredMixin, DeleteView):
    model = Produto
    template_name = 'fornecedores/produto_confirm_delete.html'
    success_url = reverse_lazy('fornecedores:produto-list')
    
    def get_queryset(self):
        return Produto.objects.filter(fornecedor=self.request.user)