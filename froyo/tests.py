from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home_page.html')

class IngredientsListPageTest(TestCase):
    def test_ingredients_list_page_returns_correct_html(self):
        response = self.client.get('/ingredients-list')
        self.assertTemplateUsed(response, 'ingredients_list.html')

class IngredientsDetailPageTest(TestCase):
    def test_ingredients_detail_page_returns_correct_html(self):
        response = self.client.get('/ingredients-detail')
        self.assertTemplateUsed(response, 'ingredients_detail.html')

class IngredientsUpdatePageTest(TestCase):
    def test_ingredients_update_page_returns_correct_html(self):
        response = self.client.get('/ingredients-update')
        self.assertTemplateUsed(response, 'ingredients_update_form.html')

class IngredientsCreatePageTest(TestCase):
    def test_ingredients_create_page_returns_correct_html(self):
        response = self.client.get('/ingredients-create')
        self.assertTemplateUsed(response, 'ingredients_create_form.html')
