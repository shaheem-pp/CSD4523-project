from django.urls import path

from appAuth.views import home

urlpatterns = [
    path("", home, name="home"),
]
