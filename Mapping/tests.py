from django.test import TestCase
from django.urls import reverse
from DjangoProjectexposer.models import Client, Adresse


class ClientViewTests(TestCase):

    def setUp(self):
        # Créer un client de test
        self.client_test = Client.objects.create(
            nom="TestNom",
            prenom="TestPrenom",
            email="test@example.com",
            img_client="test_image.jpg"
        )

        # URL pour les différentes vues
        self.home_url = reverse('home')
        self.form_url = reverse('form')
        self.adresse_choice_url = reverse('ajouter_adresse', args=[self.client_test.id_client])
        self.list_client_url = reverse('list_client')
        self.client_details_url = reverse('client', args=[self.client_test.id_client])
        self.supprimer_client_url = reverse('supprimer_client', args=[self.client_test.id_client])
        self.modifier_client_url = reverse('modifier_client', args=[self.client_test.id_client])

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    def test_form_view_get(self):
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_form_view_post(self):
        post_data = {
            'nom': 'NouveauNom',
            'prenom': 'NouveauPrenom',
            'email': 'nouveau@example.com',
        }
        response = self.client.post(self.form_url, data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Client.objects.filter(nom='NouveauNom').exists())

    def test_adresse_choice_view_get(self):
        response = self.client.get(self.adresse_choice_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Adresse_Choice.html')

    def test_adresse_choice_view_post(self):
        post_data = {
            'num_rue': '123',
            'nom_rue': 'Test Rue',
            'city': 'Test Ville',
            'state': 'Test État',
            'longitude': '12.34',
            'latitude': '56.78',
        }
        response = self.client.post(self.adresse_choice_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Adresse.objects.filter(nom_rue='Test Rue').exists())

    def test_client_list_view(self):
        response = self.client.get(self.list_client_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Client_list.html')

    def test_client_details_view(self):
        response = self.client.get(self.client_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Client_details.html')

    def test_supprimer_client_view_post(self):
        response = self.client.post(self.supprimer_client_url, data={'supprimer': True})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Client.objects.filter(id_client=self.client_test.id_client).exists())

    def test_modifier_client_view_get(self):
        response = self.client.get(self.modifier_client_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modifier_client.html')

    def test_modifier_client_view_post(self):
        post_data = {
            'nom': 'NomModifie',
            'prenom': 'PrenomModifie',
            'email': 'modifie@example.com',
        }
        response = self.client.post(self.modifier_client_url, data=post_data)
        self.assertEqual(response.status_code, 302)
        client = Client.objects.get(id_client=self.client_test.id_client)
        self.assertEqual(client.nom, 'NomModifie')
        self.assertEqual(client.prenom, 'PrenomModifie')
