from django.urls import path

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
]
