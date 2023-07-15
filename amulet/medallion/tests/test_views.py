from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.main_page_url = reverse('runes_func')
        self.style_page_url = reverse('amulet:rune_create_design')
        self.name_page_url = reverse('amulet:rune_create_name')
        self.qualities_page_url = reverse('amulet:rune_qualities')
        self.goals_page_url = reverse('amulet:rune_goals')
        self.result_page_url = reverse('amulet:rune_result')
        self.material_page_url = reverse('amulet:rune_material')
        self.final_page_url = reverse('amulet:sorry_page')

    def test_land_page(self):
        response = self.client.get(self.main_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/runes_main_page.html')

    def test_style(self):
        response = self.client.get(self.style_page_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_creation.html')

    def test_name(self):
        response = self.client.get(self.name_page_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_creation_two.html')

    def test_qualities(self):
        response = self.client.get(self.qualities_page_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_creation_three.html')

    def test_goals(self):
        response = self.client.get(self.goals_page_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_creation_four.html')

    def test_result(self):
        session_data = {
            'style': 'Troll cross',
            'combine_result': ['Ansuz', 'Gebo', 'Algiz', 'Raidho', 'Ingwaz', 'Tiwaz', 'Uruz', 'Sowilo', 'Tiwaz',
                               'Naudhiz', 'Eihwaz', 'Ansuz', 'Eihwaz', 'Raidho', 'Algiz', 'Tiwaz', 'Eihwaz', 'Ansuz',
                               'Dagaz', 'Ansuz', 'Kenaz', 'Mannaz', 'Dagaz', 'Othala'],
        }

        session = self.client.session
        session.update(session_data)
        session.save()

        response = self.client.get(self.result_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_result.html')

    def test_result_redirect(self):
        response = self.client.get(self.result_page_url)
        self.assertRedirects(response, self.style_page_url, fetch_redirect_response=False)

    def test_material(self):
        session_data = {
            'name': 'maito',
            'last_name': 'Gai',
            'combine_result': ['Ansuz', 'Gebo', 'Algiz', 'Raidho', 'Ingwaz', 'Tiwaz', 'Uruz', 'Sowilo', 'Tiwaz',
                               'Naudhiz', 'Eihwaz', 'Ansuz', 'Eihwaz', 'Raidho', 'Algiz', 'Tiwaz', 'Eihwaz', 'Ansuz',
                               'Dagaz', 'Ansuz', 'Kenaz', 'Mannaz', 'Dagaz', 'Othala'],
            'style': 'Troll cross',
            'material': 'Silver'
        }

        session = self.client.session
        session.update(session_data)
        session.save()

        response = self.client.get(self.material_page_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/rune_matter.html')

    def test_material_redirect(self):
        response = self.client.get(self.material_page_url)
        self.assertRedirects(response, self.style_page_url, fetch_redirect_response=False)

    def test_final(self):
        session_data = {
            'name': 'maito',
            'last_name': 'Gai',
            'combine_result': ['Ansuz', 'Gebo', 'Algiz', 'Raidho', 'Ingwaz', 'Tiwaz', 'Uruz', 'Sowilo', 'Tiwaz',
                               'Naudhiz', 'Eihwaz', 'Ansuz', 'Eihwaz', 'Raidho', 'Algiz', 'Tiwaz', 'Eihwaz', 'Ansuz',
                               'Dagaz', 'Ansuz', 'Kenaz', 'Mannaz', 'Dagaz', 'Othala'],
            'style': 'Troll cross',
            'material': 'Silver'
        }

        session = self.client.session
        session.update(session_data)
        session.save()

        response = self.client.get(self.final_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runes/sorry_page.html')

    def test_final_redirect(self):
        response = self.client.get(self.final_page_url)
        self.assertRedirects(response, self.style_page_url, fetch_redirect_response=False)
