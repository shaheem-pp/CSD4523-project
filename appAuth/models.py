import os
import random
import string
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


def get_random_string():
    chars = string.ascii_lowercase
    strin = "".join(random.choice(chars) for _ in range(6))
    date = datetime.now().strftime("%m%d%H%M%S")
    return "f" + date + strin


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)
        extra_fields.setdefault("name", "Superuser")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("user_type") != 1:
            raise ValueError("Superuser must have user_type=1.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = (
        (1, "Admin"),
        (2, "User"),
        (3, "Chef"),
    )

    def get_file_path(instance, filename):
        ext = filename.split(".")[-1]
        tmp = get_random_string()
        filename = f"{tmp}.{ext}"
        return os.path.join("user", filename)

    email = models.EmailField(
        unique=True,
        max_length=255,
        error_messages={
            "unique": _("A user with this email already exists."),
        },
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.IntegerField(default=2, choices=TYPE_CHOICES)
    image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default="user/default.jpg"
    )
    designation = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the staff can log into this site."),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def clean(self):
        if self.user_type == 3 and not self.designation:
            raise ValidationError({"designation": "Chefs must have a designation."})
        super().clean()

    def __str__(self):
        return self.email
