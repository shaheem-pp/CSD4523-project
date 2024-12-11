from django.urls import path

from appUser.views import home

urlpatterns = [
    path("", home, name="home"),
]
