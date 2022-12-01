"""MonitoraVoos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from rota import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', views.area_logada, name='home'),
    path('crud/', TemplateView.as_view(template_name='crud.html'), name='crud'),
    path('crud/criar-rota', views.RotaCreate.as_view(), name='criar-rota'),
    path('crud/consultar-rotas', views.RotaListView.as_view(), name='consultar-rota'),
    path('crud/consultar-rotas/<int:pk>', views.RotaDetailView.as_view(), name='rota-detail'),
    path('crud/atualizar-rota', views.RotaUpdateListView.as_view(), name='atualizar-rota'),
    path('crud/atualizar-rota/<int:pk>', views.RotaUpdate.as_view(), name='rota-update-form'),
    path('crud/excluir-rota', views.RotaDeleteListView.as_view(), name='excluir-rota'),
    path('crud/excluir-rota/<pk>', views.RotaDelete.as_view(), name='confirmar-excluir-rota'),
    path('crud/criar-voo', views.VooCreate.as_view(), name='criar-voo'),
    path('crud/consultar-voos', views.VooListView.as_view(), name='consultar-voo'),
    path('crud/consultar-voos/<int:pk>', views.VooDetailView.as_view(), name='voo-detail'),
    path('crud/atualizar-voo', views.VooUpdateListView.as_view(), name='atualizar-voo'),
    path('crud/atualizar-voo/<int:pk>', views.VooUpdate.as_view(), name='voo-update-form'),
    path('crud/excluir-voo', views.VooDeleteListView.as_view(), name='excluir-voo'),
    path('crud/excluir-voo/<pk>', views.VooDelete.as_view(), name='confirmar-excluir-voo'),
    path('monitoramento/', views.monitoramento, name='monitoramento'),
    path('monitoramento/<pk>', views.MonitoraVoo.as_view(), name='status-manager'),
    path('geracao-relatorios/', views.geracao_relatorios),
    # path('geracao-relatorios/voos-companhia', views.voos_companhia, name='relatorio-voos-companhia'),
    # path('geracao-relatorios/voos-destino', views.voos_destino, name='relatorio-voos-destino')
    path('geracao-relatorios/estatisticas-voos', views.estatisticas_voo, name='relatorio-voos'),
    path('geracao-relatorios/estatisticas-rotas', views.estatisticas_rota, name='relatorio-rotas')
]
