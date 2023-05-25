from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(title="Recipe 1", description="Description 1", ingredients="Ingredients 1", instructions="Instructions 1")
        # Create additional recipes or categories if needed for testing

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

