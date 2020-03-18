from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home_page.html"

class IngredientsListView(TemplateView):
    template_name = "ingredients_list.html"

class IngredientsDetailView(TemplateView):
    template_name = "ingredients_detail.html"

class IngredientsUpdateView(TemplateView):
    template_name = "ingredients_update_form.html"

class IngredientsCreateView(TemplateView):
    template_name = "ingredients_create_form.html"

class RecipesListView(TemplateView):
    template_name = "recipes_list.html"

class RecipesDetailView(TemplateView):
    template_name = "recipes_detail.html"
