from django.shortcuts import render
from django.db.models import Count
from appRecipe.models import Category, Recipe
from appUser.models import Like, Bookmark
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    categories = Category.objects.filter(is_deleted=False)
    recipes = Recipe.objects.filter(is_deleted=False).annotate(like_count=Count("like"))
    if request.user.is_authenticated:
        liked_recipes = Like.objects.filter(user=request.user).values_list(
            "recipe", flat=True
        )
        bookmarked_recipes = Bookmark.objects.filter(user=request.user).values_list(
            "recipe", flat=True
        )
        for recipe in recipes:
            recipe.is_liked = recipe.id in liked_recipes
            recipe.is_bookmarked = recipe.id in bookmarked_recipes
    else:
        for recipe in recipes:
            recipe.is_liked = False
            recipe.is_bookmarked = False

    context = {
        "title": "Recime | The Recipe App",
        "categories": categories,
        "recipes": recipes,
    }
    return render(request, "appRecipe/home.html", context=context)
