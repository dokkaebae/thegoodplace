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

class RecipesListPageTest(TestCase):
    def test_recipes_list_page_returns_correct_html(self):
        response = self.client.get('/recipes-list')
        self.assertTemplateUsed(response, 'recipes_list.html')

class RecipesDetailPageTest(TestCase):
    def test_recipes_detail_page_returns_correct_html(self):
        response = self.client.get('/recipes-detail')
        self.assertTemplateUsed(response, 'recipes_detail.html')

class RecipesUpdatePageTest(TestCase):
    def test_recipes_update_page_returns_correct_html(self):
        response = self.client.get('/recipes-update')
        self.assertTemplateUsed(response, 'recipes_update_form.html')

class RecipesCreatePageTest(TestCase):
    def test_recipes_create_page_returns_correct_html(self):
        response = self.client.get('/recipes-create')
        self.assertTemplateUsed(response, 'recipes_create_form.html')

class OrdersListPageTest(TestCase):
    def test_orders_list_page_returns_correct_html(self):
        response = self.client.get('/orders-list')
        self.assertTemplateUsed(response, 'orders_list.html')

class OrdersDetailPageTest(TestCase):
    def test_orders_detail_page_returns_correct_html(self):
        response = self.client.get('/orders-detail')
        self.assertTemplateUsed(response, 'orders_detail.html')

class OrdersUpdatePageTest(TestCase):
    def test_orders_update_page_returns_correct_html(self):
        response = self.client.get('/orders-update')
        self.assertTemplateUsed(response, 'orders_update_form.html')

class OrdersCreatePageTest(TestCase):
    def test_orders_create_page_returns_correct_html(self):
        response = self.client.get('/orders-create')
        self.assertTemplateUsed(response, 'orders_create_form.html')

class PageContainsCssTest(TestCase):
    def test_home_page_contains_css(self):
        response = self.client.get('')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_ingredients_list_contains_css(self):
        response = self.client.get('/ingredients-list')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_ingredients_detail_contains_css(self):
        response = self.client.get('/ingredients-detail')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_ingredients_update_contains_css(self):
        response = self.client.get('/ingredients-update')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_ingredients_create_contains_css(self):
        response = self.client.get('/ingredients-create')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_recipes_list_contains_css(self):
        response = self.client.get('/recipes-list')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_recipes_detail_contains_css(self):
        response = self.client.get('/recipes-detail')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_recipes_update_contains_css(self):
        response = self.client.get('/recipes-update')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)

    def test_recipes_create_contains_css(self):
        response = self.client.get('/recipes-create')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet" href="/static/bootstrap.min.css">', html)
        self.assertIn('<link rel="stylesheet" href="/static/styles.css">', html)
