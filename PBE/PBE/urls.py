"""
URL configuration for PBE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from catalogue_override import urls as catalogue_urls 
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('produtos.urls')),
    #path('fornecedor/', include('fornecedores.urls')),
    path('dashboard/fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
    #path('dashboard/', RedirectView.as_view(url='/dashboard/fornecedor/', permanent=False)),
    path('catalogue/', include(catalogue_urls)),
    path('', include(apps.get_app_config('oscar').urls[0])),  # Include the main application URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)