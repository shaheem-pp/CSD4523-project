from django.urls import path

from appRecipe import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/view/<str:slug>/", views.recipe_view, name="recipe-view"),
    path(
        "recipe/categories/<str:slug>/",
        views.category_view,
        name="recipe-category-view",
    ),
]
