from django.shortcuts import render

from appAuth.forms import LoginForm


# Create your views here.


def login(request):
    forms = LoginForm()
    context = {"title": "Login", "forms": forms}
    return render(request, "appAuth/login.html", context=context)
