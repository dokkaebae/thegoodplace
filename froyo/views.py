from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Ingredient

class HomePageView(TemplateView):
    template_name = "home_page.html"

class IngredientsListView(ListView):
    template_name = "ingredients_list.html"

    emptyIngredient = Ingredient(
        name="",
        quantity=""
    )
    emptyIngredient.save()

    queryset = Ingredient.objects.all()
    context = {
        "object_list": queryset
    }
