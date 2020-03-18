from django.urls import path

from .views import HomePageView
from .views import IngredientsListView
from .views import IngredientsDetailView
from .views import IngredientsUpdateView
from .views import IngredientsCreateView
from .views import RecipesListView
from .views import RecipesDetailView
from .views import RecipesUpdateView
from .views import RecipesCreateView
from .views import OrdersListView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('ingredients-list', IngredientsListView.as_view()),
    path('ingredients-detail', IngredientsDetailView.as_view()),
    path('ingredients-update', IngredientsUpdateView.as_view()),
    path('ingredients-create', IngredientsCreateView.as_view()),
    path('recipes-list', RecipesListView.as_view()),
    path('recipes-detail', RecipesDetailView.as_view()),
    path('recipes-update', RecipesUpdateView.as_view()),
    path('recipes-create', RecipesCreateView.as_view()),
    path('orders-list', OrdersListView.as_view())
]
