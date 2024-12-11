from django.urls import path

from appRecipe.views import home

urlpatterns = [
    path("", home, name="home"),
]
