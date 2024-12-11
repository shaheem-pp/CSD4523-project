from django.urls import path

from appAuth.views import login

urlpatterns = [
    path("/login/", login, name="login"),
]
