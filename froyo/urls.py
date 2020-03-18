from django.urls import path

from .views import HomePageView
from .views import IngredientsListView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('ingredients-list', IngredientsListView.as_view())
]
