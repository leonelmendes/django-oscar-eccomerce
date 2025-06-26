from oscar.core.application import OscarDashboardConfig
from django.urls import path
from fornecedores.views import FornecedorDashboardView
from oscar.apps.dashboard.nav import register_core_app
from oscar.apps.dashboard.nav import DashboardNav

# 1) Registra seu app como “core” do dashboard
register_core_app(
    namespace='fornecedores',      # deve bater com o app_name nas suas urls.py
    title='Fornecedores',
    icon='icon-sitemap'
)

class FornecedoresDashboardConfig(OscarDashboardConfig):
    label = 'fornecedores_dashboard'
    name = 'fornecedores'
    namespace = 'fornecedores_dashboard'
    
    def get_urls(self):
        urls = [
            path('', FornecedorDashboardView.as_view(), name='fornecedores-dashboard'),
            # Adicione outras URLs aqui
        ]
        return self.post_process_urls(urls)

    default_permissions = ['is_staff']