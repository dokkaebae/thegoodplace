from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_display_home_page_and_each_model_templates(self):
        #Go to home page and look at title
        self.browser.get("http://localhost:8000")
        self.assertIn("The Good Place FroYo Shop", self.browser.title)

        #See home page header
        home_page_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            home_page_header.get_attribute("innerHTML"),
            "The Good Place FroYo Shop"
        )

        #Find the ingredients section
        home_page_ingredients = self.browser.find_element_by_id("home_page_ingredients")
        self.assertEqual(
            home_page_ingredients.get_attribute("innerHTML"),
            "Ingredients"
        )

        #Find button and go to ingredients list
        button_to_ingredients = self.browser.find_element_by_id("button_to_ingredients")
        button_to_ingredients.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-list",
            self.browser.current_url
        )

        #Look at ingredients list title and header
        self.assertIn("Ingredients - List", self.browser.title)
        ingredients_list_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            ingredients_list_header.get_attribute("innerHTML"),
            "Ingredients - List"
        )

        #Find and click button to ingredients detail
        button_to_ingredients_detail = self.browser.find_element_by_id("button_to_ingredients_detail")
        button_to_ingredients_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-detail",
            self.browser.current_url
        )

        #Look at ingredients detail title and header
        self.assertIn("Ingredients - Detail", self.browser.title)
        ingredients_detail_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            ingredients_detail_header.get_attribute("innerHTML"),
            "Ingredients - Detail"
        )

        #Find and click button to ingredients update
        button_to_ingredients_update = self.browser.find_element_by_id("button_to_ingredients_update")
        button_to_ingredients_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-update",
            self.browser.current_url
        )

        #Look at ingredients update title and header
        self.assertIn("Ingredients - Update", self.browser.title)
        ingredients_update_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            ingredients_update_header.get_attribute("innerHTML"),
            "Ingredients - Update"
        )

        #Find and click back button to igredients detail
        back_button_to_ingredients_detail_from_update = self.browser.find_element_by_id("back_button")
        back_button_to_ingredients_detail_from_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-detail",
            self.browser.current_url
        )

        #Find and click back button to igredients list
        back_button_to_ingredients_list_from_detail = self.browser.find_element_by_id("back_button")
        back_button_to_ingredients_list_from_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-list",
            self.browser.current_url
        )

        #Find and click button to ingredients create
        button_to_ingredients_create = self.browser.find_element_by_id("button_to_ingredients_create")
        button_to_ingredients_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-create",
            self.browser.current_url
        )

        #Look at ingredients update title and header
        self.assertIn("Ingredients - Create", self.browser.title)
        ingredients_create_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            ingredients_create_header.get_attribute("innerHTML"),
            "Ingredients - Create"
        )

        #Find and click back button to igredients list
        back_button_to_ingredients_list_from_create = self.browser.find_element_by_id("back_button")
        back_button_to_ingredients_list_from_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/ingredients-list",
            self.browser.current_url
        )

        #Find and click back button to home page
        back_button_to_home_from_ingredients = self.browser.find_element_by_id("back_button")
        back_button_to_home_from_ingredients.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/",
            self.browser.current_url
        )

        #Find the recipes section
        home_page_recipes = self.browser.find_element_by_id("home_page_recipes")
        self.assertEqual(
            home_page_recipes.get_attribute("innerHTML"),
            "Recipes"
        )

        #Find button and go to recipes list
        button_to_recipes = self.browser.find_element_by_id("button_to_recipes")
        button_to_recipes.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-list",
            self.browser.current_url
        )

        #Look at recipes list title and header
        self.assertIn("Recipes - List", self.browser.title)
        recipes_list_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            recipes_list_header.get_attribute("innerHTML"),
            "Recipes - List"
        )

        #Find and click button to recipes detail
        button_to_recipes_detail = self.browser.find_element_by_id("button_to_recipes_detail")
        button_to_recipes_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-detail",
            self.browser.current_url
        )

        #Look at recipes detail title and header
        self.assertIn("Recipes - Detail", self.browser.title)
        recipes_detail_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            recipes_detail_header.get_attribute("innerHTML"),
            "Recipes - Detail"
        )

        #Find and click button to recipes update
        button_to_recipes_update = self.browser.find_element_by_id("button_to_recipes_update")
        button_to_recipes_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-update",
            self.browser.current_url
        )

        #Look at recipes update title and header
        self.assertIn("Recipes - Update", self.browser.title)
        recipes_update_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            recipes_update_header.get_attribute("innerHTML"),
            "Recipes - Update"
        )

        #Find and click back button to recipes detail
        back_button_to_recipes_detail_from_update = self.browser.find_element_by_id("back_button")
        back_button_to_recipes_detail_from_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-detail",
            self.browser.current_url
        )

        #Find and click back button to recipes list
        back_button_to_recipes_list_from_detail = self.browser.find_element_by_id("back_button")
        back_button_to_recipes_list_from_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-list",
            self.browser.current_url
        )

        #Find and click button to recipes create
        button_to_recipes_create = self.browser.find_element_by_id("button_to_recipes_create")
        button_to_recipes_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-create",
            self.browser.current_url
        )

        #Look at recipes update title and header
        self.assertIn("Recipes - Create", self.browser.title)
        recipes_create_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            recipes_create_header.get_attribute("innerHTML"),
            "Recipes - Create"
        )

        #Find and click back button to recipes list
        back_button_to_recipes_list_from_create = self.browser.find_element_by_id("back_button")
        back_button_to_recipes_list_from_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/recipes-list",
            self.browser.current_url
        )

        #Find and click back button to home page
        back_button_to_home_from_recipes = self.browser.find_element_by_id("back_button")
        back_button_to_home_from_recipes.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/",
            self.browser.current_url
        )

        #Find the orders section
        home_page_orders = self.browser.find_element_by_id("home_page_orders")
        self.assertEqual(
            home_page_orders.get_attribute("innerHTML"),
            "Orders"
        )

        #Find button and go to orders list
        button_to_orders = self.browser.find_element_by_id("button_to_orders")
        button_to_orders.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-list",
            self.browser.current_url
        )

        #Look at orders list title and header
        self.assertIn("Orders - List", self.browser.title)
        orders_list_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            orders_list_header.get_attribute("innerHTML"),
            "Orders - List"
        )

        #Find and click button to orders detail
        button_to_orders_detail = self.browser.find_element_by_id("button_to_orders_detail")
        button_to_orders_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-detail",
            self.browser.current_url
        )

        #Look at orders detail title and header
        self.assertIn("Orders - Detail", self.browser.title)
        orders_detail_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            orders_detail_header.get_attribute("innerHTML"),
            "Orders - Detail"
        )

        #Find and click button to orders update
        button_to_orders_update = self.browser.find_element_by_id("button_to_orders_update")
        button_to_orders_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-update",
            self.browser.current_url
        )

        #Look at orders update title and header
        self.assertIn("Orders - Update", self.browser.title)
        orders_update_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            orders_update_header.get_attribute("innerHTML"),
            "Orders - Update"
        )

        #Find and click back button to orders detail
        back_button_to_orders_detail_from_update = self.browser.find_element_by_id("back_button")
        back_button_to_orders_detail_from_update.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-detail",
            self.browser.current_url
        )

        #Find and click back button to orders list
        back_button_to_orders_list_from_detail = self.browser.find_element_by_id("back_button")
        back_button_to_orders_list_from_detail.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-list",
            self.browser.current_url
        )

        #Find and click button to orders create
        button_to_orders_create = self.browser.find_element_by_id("button_to_orders_create")
        button_to_orders_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-create",
            self.browser.current_url
        )

        #Look at orders update title and header
        self.assertIn("Orders - Create", self.browser.title)
        orders_create_header = self.browser.find_element_by_id("page_header")
        self.assertEqual(
            orders_create_header.get_attribute("innerHTML"),
            "Orders - Create"
        )

        #Find and click back button to orders list
        back_button_to_orders_list_from_create = self.browser.find_element_by_id("back_button")
        back_button_to_orders_list_from_create.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000/orders-list",
            self.browser.current_url
        )

        #Find and click back button to home page
        back_button_to_home_from_orders = self.browser.find_element_by_id("back_button")
        back_button_to_home_from_orders.click()
        time.sleep(1)
        self.assertEqual(
            "http://localhost:8000",
            self.browser.current_url
        )

        self.fail("Finish the test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
