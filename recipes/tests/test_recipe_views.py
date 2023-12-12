from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeViewsTest(TestCase):


    def test_recipe_home_views_function_is_correct(self):
        '''
            assertIs() Verify indenty of object
            lista_1 = []
            lista_2 = lista_1
            self.assertIs()
        '''
        view = resolve(
            reverse('recipes:home')
        )
        self.assertIs(view.func, views.home)

    
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)


    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')


    def teste_recipe_home_templates_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'no recipes found',
            response.content.decode('utf-8')
        )


    def test_recipe_home_template_loads_recipes(self):
        '''
        fixture,
        code smelling
        '''
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            firt_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title = 'Recipe title',
            description = 'Recipe description',
            slug = 'Recipe slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe preparation steps',
            preparation_steps_is_html = False,
            is_published = True,
        )
        #response = self.client.get(reverse('recipes:home'))
        #response_recipes = response.context['recipes']
        #self.assertEqual(response_recipes.first().title, 'Recipe title')

        response_context_recipes = response.context['recipes']
        response = self.client.get(reverse('recipes:home'))
        response_conext = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_conext)
        self.assertIn('10 Minutos', response_conext)
        self.assertEqual(len(response_context_recipes), 1)


    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:category',  kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)


    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe',  kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)


    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
