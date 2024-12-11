from django.db import models

from appAuth.models import CustomUser
from appRecipe.models import Recipe


# Create your models here.
class Bookmark(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Bookmark: {self.user} -> {self.recipe}"


class Like(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Like: {self.user} -> {self.recipe}"


class Review(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user} on {self.recipe}"
