from django.urls import path

from appAuth import views

urlpatterns = [
    path("/login/", views.login, name="login"),
    path("/signout/", views.signout, name="signout"),
]
