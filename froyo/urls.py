from django.urls import path

from .views import HomePageView
from .views import IngredientsListView
from .views import IngredientsDetailView
from .views import IngredientsUpdateView
from .views import IngredientsCreateView
from .views import RecipesListView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('ingredients-list', IngredientsListView.as_view()),
    path('ingredients-detail', IngredientsDetailView.as_view()),
    path('ingredients-update', IngredientsUpdateView.as_view()),
    path('ingredients-create', IngredientsCreateView.as_view()),
    path('recipes-list', RecipesListView.as_view())
]
