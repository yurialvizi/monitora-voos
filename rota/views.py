from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# from rota.forms import CriarRotaForm
from rota.models import Rota, Voo, RotaForm, RotaUpdateForm, VooCreateForm, VooFuncionarioForm, VooPilotoForm, VooTorreForm, VooUpdateForm

# Create your views here.
def login(request):
    return render(request,"login.html")

def area_logada(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"area_logada.html", context)

@login_required
@permission_required('rota.add_rota', raise_exception=True)
def crud(request):
    return render(request,"crud.html")

@login_required
@permission_required('rota.view_rota')
def geracao_relatorios(request):
    return render(request,"geracao_relatorios.html")

@login_required
@permission_required('rota.change_voo', raise_exception=True)
def monitoramento(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"monitoramento.html", context)

@login_required
@permission_required('rota.view_rota')
def estatisticas_voo(request):
    voos = Voo.objects.all()
 
    piloto = {}
    for voo in voos:
        if voo.piloto in piloto:
            piloto[voo.piloto] += 1
        else:
            piloto[voo.piloto] = 1
 
    status = {}
 
    for voo in voos:
        if voo.get_status_display() in status:
            status[voo.get_status_display()] += 1
        else:
            status[voo.get_status_display()] = 1
   
    context = {
        'piloto': piloto,
        'status': status
    }
    return render(request,"geracao_relatorios/estatisticas_voo.html", context)
 
@login_required
@permission_required('rota.view_rota')
def estatisticas_rota(request):
    voos = Voo.objects.all()
 
    freq_partida = {}
    freq_chegada = {}

    for voo in voos:
        if voo.rota.destino in freq_partida:
            freq_partida[voo.rota.destino] += 1
        else:
            freq_partida[voo.rota.destino] = 1

    for voo in voos:
        if voo.rota.origem in freq_chegada:
            freq_chegada[voo.rota.origem] += 1
        else:
            freq_chegada[voo.rota.origem] = 1
 
    aeronaves = {}
 
    for voo in voos:
        if voo.rota.aeronave in aeronaves:
            aeronaves[voo.rota.aeronave] += 1
        else:
            aeronaves[voo.rota.aeronave] = 1
 
    companhia = {}
 
    for voo in voos:
        if voo.rota.companhia_aerea in companhia:
            companhia[voo.rota.companhia_aerea] += 1
        else:
            companhia[voo.rota.companhia_aerea] = 1

    freq_partida.pop('São Paulo')
    freq_chegada.pop('São Paulo')
 
    context = {
        'destinos': freq_partida,
        'origens': freq_chegada,
        'aeronaves': aeronaves,
        'companhia': companhia
    }
    return render(request,"geracao_relatorios/estatisticas_rota.html", context)



class MonitoraVoo(PermissionRequiredMixin, UpdateView):
    permission_required = 'rota.change_voo'
    model = Voo
    template_name = 'monitoramento/status_manager.html'
    success_url = reverse_lazy('monitoramento')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Piloto').exists():
            return VooPilotoForm
        elif self.request.user.groups.filter(name='Torre de Controle').exists():
            return VooTorreForm
        else:
            return VooFuncionarioForm


class RotaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'rota.add_rota'
    model = Rota
    form_class = RotaForm
    success_url = reverse_lazy('crud')

class RotaUpdateListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Rota
    template_name = 'crud/atualizar_rota.html'

class RotaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'rota.add_rota'
    model = Rota
    form_class= RotaUpdateForm
    success_url = reverse_lazy('crud')

class RotaListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Rota

class RotaDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'rota.add_rota'
    model = Rota
    template_name = 'crud/consultar_rotas/rota_detail.html'

class RotaDeleteListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Rota
    template_name = 'crud/excluir_rota.html'

class RotaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'rota.add_rota'
    model = Rota
    template_name = 'crud/excluir_rota/confirmar_excluir_rota.html'
    success_url = reverse_lazy('crud')


class VooCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'rota.add_rota'
    model = Voo
    form_class = VooCreateForm
    success_url = reverse_lazy('crud')

class VooUpdateListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Voo
    template_name = 'crud/atualizar_voo.html'

class VooUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'rota.add_rota'
    model = Voo
    form_class = VooUpdateForm
    template_name = 'crud/atualizar_voo/update_form.html'
    success_url = reverse_lazy('crud')

class VooListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Voo

class VooDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'rota.add_rota'
    model = Voo
    template_name = 'crud/consultar_voos/voo_detail.html'

class VooDeleteListView(PermissionRequiredMixin, ListView):
    permission_required = 'rota.add_rota'
    model = Voo
    template_name = 'crud/excluir_voo.html'

class VooDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'rota.add_rota'
    model = Voo
    template_name = 'crud/excluir_voo/confirmar_excluir_voo.html'
    success_url = reverse_lazy('crud')

