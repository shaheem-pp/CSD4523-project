from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from appAuth.forms import LoginForm


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LoginForm()

    context = {
        "title": "Login",
        "form": form,
    }
    return render(request, "appAuth/login.html", context)


@login_required
def signout(request):
    request.session.flush()
    return redirect("home")
