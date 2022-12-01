from django.test import TestCase

# Create your tests here.
from rota.models import Rota, Voo

class RotaModelCreateTest(TestCase): 
    @classmethod
    def setUpTestData(cls):
        Rota.objects.create(
            codigo='D0810', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
    def test_criacao_id(self):
        rota_1 = Rota.objects.get(codigo='D0810')
        self.assertEqual(rota_1.id, 1)

    def test_get_rota(self):
        rota_1 = Rota.objects.get(origem='Goiânia', destino='Rio de Janeiro', companhia_aerea='Varig')
        self.assertEqual(rota_1.codigo, 'D0810')

    def test_atualiza_rota(self):
        Rota.objects.update(
            hora_partida_prevista='08:53',
            hora_chegada_prevista='10:20'
        )
        rota_1 = Rota.objects.get(codigo='D0810')
        self.assertEqual(rota_1.hora_partida_prevista.strftime("%H:%M"), '08:53')

    def test_deleta_rota(self):
        Rota.objects.filter(codigo='D0810').delete()
        with self.assertRaises(Rota.DoesNotExist):
            Rota.objects.get(codigo='D0810')


class VooModelCreateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rota.objects.create(
            codigo='A823', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
        rota_1 = Rota.objects.get(codigo='A823')
        Voo.objects.create(
            rota=rota_1,
            data='2022-07-11',
            piloto='Comandante Denio Almeida',
            status='Programado'
        )

    def test_criacao_id(self):
        rota_1 = Rota.objects.get(codigo='A823')
        voo_1 = Voo.objects.get(rota=rota_1, data='2022-07-11')
        self.assertEqual(voo_1.id, 1)

    def test_get_voo(self):
        rota_1 = Rota.objects.get(codigo='A823')
        voo_1 = Voo.objects.get(rota=rota_1, data='2022-07-11')
        self.assertEqual(voo_1.piloto, 'Comandante Denio Almeida')

    def test_update_voo(self):
        Voo.objects.update(
            status= 'pronto'
        )
        rota_1 = Rota.objects.get(codigo='A823')
        voo_1 = Voo.objects.get(rota=rota_1, data='2022-07-11')
        self.assertEqual(voo_1.status, 'pronto')

    def test_delete_voo(self):
        tamOriginal = len(Voo.objects.all())
        Voo.objects.filter(id=1).delete()

        tamFinal = len(Voo.objects.all())
        self.assertEqual(tamFinal, tamOriginal-1)