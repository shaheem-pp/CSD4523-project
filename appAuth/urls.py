from django.urls import path

from appAuth import views

urlpatterns = [
    path("/login/", views.login, name="login"),
    path("/signout/", views.signout, name="signout"),
    path("/signup/", views.signup, name="signup"),
    path("/verify_code/", views.verify_chef, name="verify_chef"),
]
