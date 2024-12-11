from django import forms

from appAuth.models import CustomUser
from customUtils import BootstrapFormMixin


class LoginForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
