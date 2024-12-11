from django.urls import path

from appRecipe import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/view/<str:slug>/", views.recipe_view, name="recipe-view"),
]
