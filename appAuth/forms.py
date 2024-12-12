from django import forms

from appAuth.models import CustomUser
from customUtils import BootstrapFormMixin


class LoginForm(BootstrapFormMixin, forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        ),
    )


class CustomUserForm(BootstrapFormMixin, forms.ModelForm):
    enter_code = forms.CharField(required=False, max_length=20, label="Code")
    designation = forms.CharField(required=False, max_length=100, label="Designation")

    class Meta:
        model = CustomUser
        fields = ["name", "email", "password", "image", "enter_code", "designation"]
        widgets = {
            "password": forms.PasswordInput(),
        }
