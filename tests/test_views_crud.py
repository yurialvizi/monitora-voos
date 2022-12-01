from django.test import TestCase
from django.urls import reverse

# aqui testamos as views do crud

class CrudViewTest (TestCase):

#criar rota
    def test_view_criar_rota_avaible(self):
        response = self.client.get(reverse('criar-rota'))
        self.assertEqual(response.status_code, 200)

    def test_view_criar_rota_template(self):
        response = self.client.get(reverse('criar-rota'))
        self.assertTemplateUsed(response,'rota/rota_form.html' )


#consultar rota

    def test_view_consultar_rota_avaible(self):
        response = self.client.get(reverse('consultar-rota'))
        self.assertEqual(response.status_code, 200)

    def test_view_consultar_rota_template(self):
        response = self.client.get(reverse('consultar-rota'))
        self.assertTemplateUsed(response,'rota/rota_list.html' )

# atualizar rota

    def test_view_atualizar_rota_avaible(self):
        response = self.client.get(reverse('atualizar-rota'))
        self.assertEqual(response.status_code, 200)

    def test_view_atualizar_rota_template(self):
        response = self.client.get(reverse('atualizar-rota'))
        self.assertTemplateUsed(response,'crud/atualizar_rota.html' )

    def test_view_atualizar_rota_content(self):
        response = self.client.get(reverse('atualizar-rota'))
        self.assertContains(response, "<h2>Rotas </h2>")
        self.assertNotContains(response, "Not on the page")

# excluir rota

    def test_view_excluir_rota_avaible(self):
        response = self.client.get(reverse('excluir-rota'))
        self.assertEqual(response.status_code, 200)

    def test_view_excluir_rota_template(self):
        response = self.client.get(reverse('excluir-rota'))
        self.assertTemplateUsed(response,'crud/excluir_rota.html' )

    def test_view_excluir_rota_content(self):
        response = self.client.get(reverse('excluir-rota'))
        self.assertContains(response, "Excluir Rota")
        self.assertNotContains(response, "Not on the page")

# criar voo
    def test_view_criar_voo_avaible(self):
        response = self.client.get(reverse('criar-voo'))
        self.assertEqual(response.status_code, 200)

    def test_view_criar_voo_template(self):
        response = self.client.get(reverse('criar-voo'))
        self.assertTemplateUsed(response,'rota/voo_form.html' )

#consultar voo

    def test_view_consultar_voo_avaible(self):
        response = self.client.get(reverse('consultar-voo'))
        self.assertEqual(response.status_code, 200)

    def test_view_consultar_voo_template(self):
        response = self.client.get(reverse('consultar-voo'))
        self.assertTemplateUsed(response,'rota/voo_list.html' )

# atualizar voo

    def test_view_atualizar_voo_avaible(self):
        response = self.client.get(reverse('atualizar-voo'))
        self.assertEqual(response.status_code, 200)

    def test_view_atualizar_voo_template(self):
        response = self.client.get(reverse('atualizar-voo'))
        self.assertTemplateUsed(response,'crud/atualizar_voo.html' )

    def test_view_atualizar_voo_content(self):
        response = self.client.get(reverse('atualizar-voo'))
        self.assertContains(response, "<h2>Voos </h2>")
        self.assertNotContains(response, "Not on the page")

# excluir voo

    def test_view_excluir_voo_avaible(self):
        response = self.client.get(reverse('excluir-voo'))
        self.assertEqual(response.status_code, 200)

    def test_view_excluir_voo_template(self):
        response = self.client.get(reverse('excluir-voo'))
        self.assertTemplateUsed(response,'crud/excluir_voo.html' )

    def test_view_excluir_voo_content(self):
        response = self.client.get(reverse('excluir-voo'))
        self.assertContains(response, "Excluir Voo")
        self.assertNotContains(response, "Not on the page")

