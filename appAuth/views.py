from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from appAuth.forms import LoginForm, CustomUserForm


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


# def verify_chef(request):
#
#     if request.method == "POST":
#         code = request.POST.get("code", "").strip()
#
#         # Check if the entered code is valid
#         if code in VALID_CODES:
#             return JsonResponse({"is_valid": True})
#         else:
#             return JsonResponse({"is_valid": False})
#
#     return JsonResponse({"is_valid": False})


def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            # if 'enter_code' in form.cleaned_data:
            #     if user.designation and form.cleaned_data["enter_code"] in VALID_CODES:
            #         user.user_type = 3

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
            messages.error(request, "Form is not valid. Please check your input.")
            return render(request, "appAuth/signup.html", {"form": form})
    else:
        form = CustomUserForm()
    return render(request, "appAuth/signup.html", {"form": form})
