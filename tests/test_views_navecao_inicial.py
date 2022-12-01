from django.test import TestCase
from django.urls import reverse



# Essa primeira classe testa a pagina da area logada,
# a de gerenciamento de voos (crud), monitoramento e a de relatorios
  
class NavegacaoInicialViewTest (TestCase):
  
# home page
    def test_view_home_page_avaible(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'area_logada.html' )

    def test_view_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "<title>Área logada</title>")
        self.assertNotContains(response, "Not on the page")
#crud
    def test_view_crud_avaible(self):
        response = self.client.get(reverse('crud'))
        self.assertEqual(response.status_code, 200)

    def test_view_crud_template(self):
        response = self.client.get(reverse('crud'))
        self.assertTemplateUsed(response,'crud.html' )

    def test_view_crud_content(self):
        response = self.client.get(reverse('crud'))
        self.assertContains(response, "Cadastramento CRUD")
        self.assertNotContains(response, "Not on the page") 

# monitoramento
    def test_view_monitoramento_avaible(self):
        response = self.client.get(reverse('monitoramento'))
        self.assertEqual(response.status_code, 200)

    def test_view_monitoramento_template(self):
        response = self.client.get(reverse('monitoramento'))
        self.assertTemplateUsed(response,'monitoramento.html' )

    def test_view_monitoramento_content(self):
        response = self.client.get(reverse('monitoramento'))
        self.assertContains(response, "Escolha o voo a ser atualizado</p>")
        self.assertNotContains(response, "Not on the page")

# gerar relatorios
    def test_view_relatorios_avaible(self):
        response = self.client.get('/geracao-relatorios/')
        self.assertEqual(response.status_code, 200)

    def test_view_relatorios_template(self):
        response = self.client.get('/geracao-relatorios/')
        self.assertTemplateUsed(response,'geracao_relatorios.html' )

    def test_view_relatorios_content(self):
        response = self.client.get('http://127.0.0.1:8000/geracao-relatorios/')
        self.assertContains(response, " <title>Geração de Relatórios</title>")
        self.assertNotContains(response, "Not on the page")
