from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Ingredient

class HomePageView(TemplateView):
    template_name = "home_page.html"

class IngredientsListView(ListView):
    template_name = "ingredients_list.html"

    Ingredient.objects.all().delete()
    emptyIngredient = Ingredient(
        name="",
        quantity=""
    )
    emptyIngredient.save()

    queryset = Ingredient.objects.all()
    context = {
        "object_list": queryset
    }

class IngredientsDetailView(TemplateView):
    template_name = "ingredients_detail.html"

class IngredientsUpdateView(TemplateView):
    template_name = "ingredients_update_form.html"

class IngredientsCreateView(TemplateView):
    template_name = "ingredients_create_form.html"
