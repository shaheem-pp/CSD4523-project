from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from appAuth.forms import LoginForm, CustomUserForm


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


def verify_chef(request):
    valid_codes = ["CHEF12", "45CHE6", "FEED10"]

    if request.method == "POST":
        code = request.POST.get("code", "").strip()

        # Check if the entered code is valid
        if code in valid_codes:
            return JsonResponse({"is_valid": True})
        else:
            return JsonResponse({"is_valid": False})

    return JsonResponse({"is_valid": False})


def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            # If the user is a chef, the 'designation' field will be required
            if user.user_type == 3:
                designation = form.cleaned_data.get("designation")
                if not designation:
                    form.add_error("designation", "Designation is required for chefs.")
                    return render(request, "appAuth/signup.html", {"form": form})
                user.designation = designation

            # Set password
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Authenticate the user with the provided email and password
            user = authenticate(
                request, email=user.email, password=form.cleaned_data["password"]
            )

            if user is not None:
                auth_login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            return render(request, "appAuth/signup.html", {"form": form})
    else:
        form = CustomUserForm()
    return render(request, "appAuth/signup.html", {"form": form})
