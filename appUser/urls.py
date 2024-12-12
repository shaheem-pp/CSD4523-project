from django.urls import path

from appUser import views

urlpatterns = [
    path("/toggle_like/", views.toggle_like, name="toggle_like"),
    path("/toggle_bookmark/", views.toggle_bookmark, name="toggle_bookmark"),
    path("/settings/", views.settings, name="user_settings"),
]
