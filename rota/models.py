from django.db import models
from django.forms import ModelForm
from django import forms
import datetime
# Create your models here.
class Rota(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15, null = False, unique = True)
    aeroporto_partida = models.CharField(max_length=200, null=False)
    aeroporto_chegada = models.CharField(max_length=200, null=False)
    hora_partida_prevista= models.TimeField(auto_now=False)
    hora_chegada_prevista= models.TimeField(auto_now=False)
    origem = models.CharField(max_length=20, null=False)
    destino = models.CharField(max_length=20, null=False)
    aeronave = models.CharField(max_length=20, null=False)
    companhia_aerea = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'rotas'



class Voo(models.Model):
    STATUS_POSSIVEIS = (
        ('em', 'embarcando'),
        ('ca', 'cancelado'),
        ('pr', 'programado'),
        ('ta', 'taxiando'),
        ('pt', 'pronto'),
        ('ao', 'autorizado'),
        ('vo', 'em_voo'),
        ('at', 'aterrisado')
    )
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, null=True)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=2, null=True, blank=True, choices=STATUS_POSSIVEIS)
    piloto = models.CharField(max_length=20, null=False)
    hora_partida = models.TimeField(auto_now=False, null=True, blank=True)
    hora_chegada = models.TimeField(auto_now=False, null=True, blank=True)
    data = models.DateTimeField(null=True)
    class Meta:
        db_table = 'voos'


class RotaForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Rota    
 
        # Custom fields
        fields = '__all__'
 
    # this function will be used for the validation
    def clean(self):

        super(RotaForm, self).clean()

        hora_partida_prevista = self.cleaned_data.get('hora_partida_prevista')
        hora_chegada_prevista = self.cleaned_data.get('hora_chegada_prevista')
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        aeroporto_partida = self.cleaned_data.get('aeroporto_partida')
        aeroporto_chegada = self.cleaned_data.get('aeroporto_chegada')

        if hora_partida_prevista > hora_chegada_prevista:
            self._errors['hora_chegada_prevista'] = self.error_class([
                'Hora de chegada deve ser maior que hora de partida'])

        if origem == destino:
            self._errors['destino'] = self.error_class([
                'Destino deve ser diferente de origem'])

        if aeroporto_chegada == aeroporto_partida:
            self._errors['aeroporto_partida'] = self.error_class([
                'Aeroporto destino deve ser diferente do aeroporto de origem'])

        if aeroporto_chegada != "Guarulhos" and aeroporto_partida != "Guarulhos":
            self._errors['aeroporto_partida'] = self.error_class([
                'Origem ou destino deve ser o aeroporto de Guarulhos'
            ])
            self._errors['aeroporto_chegada'] = self.error_class([
                'Origem ou destino deve ser o aeroporto de Guarulhos'
            ])

        if origem != "São Paulo" and destino != "São Paulo":
            self._errors['origem'] = self.error_class([
                'Origem ou destino deve ser São Paulo'
            ])
            self._errors['destino'] = self.error_class([
                'Origem ou destino deve ser São Paulo'
            ])

        return self.cleaned_data


class RotaUpdateForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Rota    
 
        # Custom fields
        fields = ['aeronave', 'hora_partida_prevista', 'hora_chegada_prevista']
 
    # this function will be used for the validation
    def clean(self):

        super(RotaUpdateForm, self).clean()

        hora_partida_prevista = self.cleaned_data.get('hora_partida_prevista')
        hora_chegada_prevista = self.cleaned_data.get('hora_chegada_prevista')


        if hora_partida_prevista > hora_chegada_prevista:
            self._errors['hora_chegada_prevista'] = self.error_class([
                'Hora de chegada deve ser maior que hora de partida'])

        return self.cleaned_data

class VooUpdateForm(ModelForm):

    class Meta:
        # write the name of models for which the form is made
        model = Voo    
 
        # Custom fields
        fields = ['data', 'piloto']
    


class VooCreateForm(ModelForm):
    class Meta:
        model = Voo
        fields = ['rota', 'status', 'id', 'piloto', 'hora_partida', 'data']
    
    def clean(self):
        super(VooCreateForm, self).clean()

        rota = self.cleaned_data.get('rota')

        if rota.aeroporto_chegada == 'Guarulhos':
            self.cleaned_data['status'] = 'vo'
        else:
            self.cleaned_data['hora_partida'] = None

        return self.cleaned_data



class VooFuncionarioForm(ModelForm):

    class Meta:
        model = Voo

        fields = ['status']

    def clean(self):

        super(VooFuncionarioForm, self).clean()

        primeiro_status = ['embarcando', 'cancelado']
        
        voo = self.instance
        status_anterior =  self.instance.get_status_display()
        status_novo = self.cleaned_data.get('status')

        if voo.rota.aeroporto_partida == 'Guarulhos':
            if str(status_anterior) not in ['None', 'embarcando']:
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'None' and status_novo not in primeiro_status:
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'embarcando' and status_novo != 'pr':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
        else:
            self._errors['status'] = self.error_class(['Mudança de status não permitida'])

        return self.cleaned_data

class VooTorreForm(ModelForm):
    class Meta:
        model = Voo

        fields = ['status', 'hora_chegada', 'hora_partida']

    def clean(self):

        super(VooTorreForm, self).clean()

        status_iniciais = ['pronto', 'programado', 'em_voo']

        voo = self.instance

        status_anterior =  self.instance.get_status_display()
        status_novo = self.cleaned_data.get('status')

        if voo.rota.aeroporto_partida == 'Guarulhos':
            if status_anterior not in status_iniciais:
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'pronto' and status_novo != 'ao':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'pronto' and status_novo == 'ao' and not self.cleaned_data.get('hora_partida'):
                self._errors['hora_partida'] = self.error_class(['Hora de partida é obrigatória'])
            elif status_anterior == 'pronto' and status_novo == 'ao' and self.cleaned_data.get('hora_partida') < voo.rota.hora_partida_prevista:
                self._errors['hora_partida'] = self.error_class(['Hora de partida deve ser posterior ao horário de partida previsto'])
            elif status_anterior == 'programado' and status_novo != 'ta':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'em_voo' and status_novo != 'at':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'em_voo' and status_novo == 'at' and not self.cleaned_data.get('hora_chegada'):
                self._errors['hora_chegada'] = self.error_class(['Horário de chegada é obrigatório'])
            elif status_anterior == 'em_voo' and status_novo == 'at' and self.cleaned_data.get('hora_chegada') < voo.hora_partida:
                self._errors['hora_chegada'] = self.error_class(['Horário de chegada deve ser posterior ao horário de partida'])
        else:
            if status_anterior != 'em_voo':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'em_voo' and status_novo != 'at':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'em_voo' and status_novo == 'at' and not self.cleaned_data.get('hora_chegada'):
                self._errors['hora_chegada'] = self.error_class(['Horário de chegada é obrigatório'])
            elif status_anterior == 'em_voo' and status_novo == 'at' and self.cleaned_data.get('hora_chegada') < voo.hora_partida:
                self._errors['hora_chegada'] = self.error_class(['Horário de chegada deve ser posterior ao horário de partida'])

        if not self.cleaned_data.get('hora_partida'):
                self.cleaned_data['hora_partida'] = voo.hora_partida

        return self.cleaned_data

class VooPilotoForm(ModelForm):
    class Meta:
        model = Voo

        fields = ['status']

    def clean(self):

        super(VooPilotoForm, self).clean()

        status_iniciais = ['taxiando', 'autorizado']

        voo = self.instance
        status_anterior =  self.instance.get_status_display()
        status_novo = self.cleaned_data.get('status')

        if voo.rota.aeroporto_partida == 'Guarulhos':
            if status_anterior not in status_iniciais:
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'taxiando' and status_novo != 'pt':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
            elif status_anterior == 'autorizado' and status_novo != 'vo':
                self._errors['status'] = self.error_class(['Mudança de status não permitida'])
        else:
            self._errors['status'] = self.error_class(['Mudança de status não permitida'])

        return self.cleaned_data
