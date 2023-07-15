from django.test import SimpleTestCase
from django.urls import resolve, reverse
from medallion.views import rune_create_design, rune_create_name,\
    rune_qualities, rune_goals, rune_result, rune_material, rune_final


class TestUrls(SimpleTestCase):

    def test_design_url_resolved(self):
        url = reverse('amulet:rune_create_design')
        self.assertEquals(resolve(url).func, rune_create_design)

    def test_name_url_resolved(self):
        url = reverse('amulet:rune_create_name')
        self.assertEquals(resolve(url).func, rune_create_name)

    def test_qualities_url_resolved(self):
        url = reverse('amulet:rune_qualities')
        self.assertEquals(resolve(url).func, rune_qualities)

    def test_goals_url_resolved(self):
        url = reverse('amulet:rune_goals')
        self.assertEquals(resolve(url).func, rune_goals)

    def test_result_url_resolved(self):
        url = reverse('amulet:rune_result')
        self.assertEquals(resolve(url).func, rune_result)

    def test_material_url_resolved(self):
        url = reverse('amulet:rune_material')
        self.assertEquals(resolve(url).func, rune_material)

    def test_final_url_resolved(self):
        url = reverse('amulet:sorry_page')
        self.assertEquals(resolve(url).func, rune_final)
