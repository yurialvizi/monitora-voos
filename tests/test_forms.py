from django.test import TestCase
from django.urls import reverse

class FormsTest (TestCase):
    def test_login_form_username_field_label(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "Username")
    
    def test_login_form_username_field_placeholder(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "Enter username")

    def test_login_form_password_field_label(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "Password")

    def test_login_form_password_field_placeholder(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "Password")
