from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

class RecipeTestBase(TestCase):

    def setUp(self) -> None:
        self.make_recipe()
        return super().setUp()
    

    def make_category(self, name='Categoria'):
        return Category.objects.create(name=name)
    
    def make_author(
            self,
            firt_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        ):
        User.objects.create_user(
            firt_name=firt_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    
    def make_recipe(
        self,
        category_data=None,
        author_data=None,
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
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published
        )