from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from appRecipe.models import Category, Recipe
from appUser.models import Like, Bookmark


def get_common_context():
    categories = Category.objects.filter(is_deleted=False)

    return {"categories": categories}


# Create your views here.
def home(request):
    context = get_common_context()
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

    context.update(
        {
            "title": "Recime | The Recipe App",
            "recipes": recipes,
        }
    )
    return render(request, "appRecipe/home.html", context=context)


def recipe_view(request, slug):
    context = get_common_context()
    recipe = get_object_or_404(Recipe, slug=slug, is_deleted=False)
    like_count = Like.objects.filter(recipe=recipe, is_deleted=False).count()
    context.update(
        {"title": f"{recipe.name} | Recime", "recipe": recipe, "like_count": like_count}
    )
    if request.user.is_authenticated:
        liked_recipes = Like.objects.filter(
            user=request.user, recipe=recipe, is_deleted=False
        )
        bookmarked_recipes = Bookmark.objects.filter(
            user=request.user, recipe=recipe, is_deleted=False
        )
        context.update(
            {
                "is_liked": liked_recipes.exists(),
                "is_bookmarked": bookmarked_recipes.exists(),
            }
        )

    return render(request, "appRecipe/recipe_view.html", context=context)


def category_view(request, slug):
    context = get_common_context()
    category = get_object_or_404(Category, slug=slug, is_deleted=False)

    recipes = Recipe.objects.filter(category=category, is_deleted=False).annotate(
        like_count=Count("like")
    )
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

    context.update(
        {
            "title": f"{category.name} | Recime",
            "recipes": recipes,
        }
    )
    return render(request, "appRecipe/recipe_view.html", context=context)
