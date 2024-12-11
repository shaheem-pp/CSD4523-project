import os
import random
import string
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils.crypto import get_random_string

from appAuth.models import CustomUser


# Create your models here.
def get_random_string():
    chars = string.ascii_lowercase
    strin = "".join(random.choice(chars) for _ in range(6))
    date = datetime.now().strftime("%m%d%H%M%S")
    return "f" + date + strin


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    def get_file_path(instance, filename):
        ext = filename.split(".")[-1]
        tmp = get_random_string()
        filename = f"{tmp}.{ext}"
        return os.path.join("recipe", filename)

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default="recipe/default.jpg"
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Recipe: {self.name} by {self.author}"
