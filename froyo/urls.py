from django.urls import path

from .views import HomePageView
from .views import IngredientsListView
from .views import IngredientsDetailView
from .views import IngredientsUpdateView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('ingredients-list', IngredientsListView.as_view()),
    path('ingredients-detail', IngredientsDetailView.as_view()),
    path('ingredients-update', IngredientsUpdateView.as_view())
]
