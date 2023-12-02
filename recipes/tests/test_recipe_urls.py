from django.test import TestCase
from django.urls import reverse



# Create your tests here.
class RecipeURLsTests(TestCase):
    
    #def test_the_pytests_is_ok(self):
    #    assert 1 == 1


    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')


    def test_recipe_category_id_home_url_is_correct(self):
        url = reverse('recipes:category',  kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')


    def test_recipe_detail_home_url_is_correct(self):
        url = reverse('recipes:recipe',  kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')