from django.urls import path

from appRecipe import views as appRecipeViews
from appUser import views

urlpatterns = [
    path("/toggle_like/", views.toggle_like, name="toggle_like"),
    path("/toggle_bookmark/", views.toggle_bookmark, name="toggle_bookmark"),
    path("/settings/", views.settings, name="user_settings"),
    path(
        "/recipe/<str:recipe_slug>/add_review/",
        views.add_review,
        name="recipe_add_review",
    ),
    path(
        "/recipe/<slug:recipe_slug>/delete_review/",
        views.delete_review,
        name="delete_review",
    ),
    path("/chef/verification/", views.chef_verify, name="user_chef_verify"),
    path(
        "/update_user_details/", views.update_user_details, name="update_user_details"
    ),
    path(
        "/settings/my-recipes/", views.settings_my_recipes, name="settings_my_recipes"
    ),
    path(
        "/settings/my-bookmarks/",
        views.settings_my_bookmarks,
        name="settings_my_bookmarks",
    ),
    path("/remove_bookmark/<int:id>/", views.remove_bookmark, name="remove_bookmark"),
    path(
        "/update_recipe/<str:slug>/",
        appRecipeViews.update_recipe,
        name="update-recipe",
    ),
    path(
        "/remove_recipe/<str:slug>/",
        appRecipeViews.remove_recipe,
        name="remove-recipe",
    ),
]
