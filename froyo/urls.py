from django.urls import path

from .views import HomePageView
from .views import IngredientsListView
from .views import IngredientsDetailView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('ingredients-list', IngredientsListView.as_view()),
    path('ingredients-detail', IngredientsDetailView.as_view())
]
