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
