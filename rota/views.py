from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django import forms
# from django.contrib.auth.decorators import login_required, permission_required

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

def crud(request):
    return render(request,"crud.html")

def geracao_relatorios(request):
    return render(request,"geracao_relatorios.html")

def monitoramento(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"monitoramento.html", context)


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
 
def estatisticas_rota(request):
    voos = Voo.objects.all()
 
    freq = {}

    for voo in voos:
        if voo.rota.destino in freq:
            freq[voo.rota.destino] += 1
        else:
            freq[voo.rota.destino] = 1
 
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
 
    context = {
        'destinos': freq,
        'aeronaves': aeronaves,
        'companhia': companhia
    }
    return render(request,"geracao_relatorios/estatisticas_rota.html", context)



class MonitoraVoo(UpdateView):
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


class RotaCreate(CreateView):
    model = Rota
    form_class = RotaForm
    success_url = reverse_lazy('crud')

class RotaUpdateListView(ListView):
    model = Rota
    template_name = 'crud/atualizar_rota.html'

class RotaUpdate(UpdateView):
    model = Rota
    form_class= RotaUpdateForm
    success_url = reverse_lazy('crud')

class RotaListView(ListView):
    model = Rota

class RotaDetailView(DetailView):
    model = Rota
    template_name = 'crud/consultar_rotas/rota_detail.html'

class RotaDeleteListView(ListView):
    model = Rota
    template_name = 'crud/excluir_rota.html'

class RotaDelete(DeleteView):
    model = Rota
    template_name = 'crud/excluir_rota/confirmar_excluir_rota.html'
    success_url = reverse_lazy('crud')


class VooCreate(CreateView):
    model = Voo
    form_class = VooCreateForm
    success_url = reverse_lazy('crud')

class VooUpdateListView(ListView):
    model = Voo
    template_name = 'crud/atualizar_voo.html'

class VooUpdate(UpdateView):
    model = Voo
    form_class = VooUpdateForm
    success_url = reverse_lazy('crud')

class VooListView(ListView):
    model = Voo

class VooDetailView(DetailView):
    model = Voo
    template_name = 'crud/consultar_voos/voo_detail.html'

class VooDeleteListView(ListView):
    model = Voo
    template_name = 'crud/excluir_voo.html'

class VooDelete(DeleteView):
    model = Voo
    template_name = 'crud/excluir_voo/confirmar_excluir_voo.html'
    success_url = reverse_lazy('crud')

