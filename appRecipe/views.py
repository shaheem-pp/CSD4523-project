from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from appRecipe.forms import RecipeCreateForm
from appRecipe.models import Category, Recipe
from appUser.models import Like, Bookmark, Review


def get_common_context():
    categories = Category.objects.filter(is_deleted=False)

    return {"categories": categories}


# Create your views here.
def home(request):
    context = get_common_context()
    recipes = Recipe.objects.filter(is_deleted=False).annotate(like_count=Count("like"))
    if request.user.is_authenticated:
        liked_recipes = Like.objects.filter(
            user=request.user, recipe__is_deleted=False, user__is_deleted=False
        ).values_list("recipe", flat=True)
        bookmarked_recipes = Bookmark.objects.filter(
            user=request.user, recipe__is_deleted=False, user__is_deleted=False
        ).values_list("recipe", flat=True)
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
    recipe = get_object_or_404(
        Recipe.objects.filter(slug=slug, author__is_deleted=False, is_deleted=False)
    )

    like_count = Like.objects.filter(
        recipe=recipe,
        recipe__is_deleted=False,
        user__is_deleted=False,
        is_deleted=False,
    ).count()
    reviews = (
        Review.objects.filter(
            recipe=recipe,
            recipe__is_deleted=False,
            user__is_deleted=False,
            is_deleted=False,
        )
        .annotate(
            is_chef=Case(
                When(user__user_type=3, then=Value(1)),  # Chef gets priority
                default=Value(0),  # Non-chefs
                output_field=IntegerField(),
            )
        )
        .order_by("-is_chef", "-created_on")  # Sort by chef first, then by most recent
        .select_related("user")
    )

    context.update(
        {
            "title": f"{recipe.name} | Recime",
            "recipe": recipe,
            "like_count": like_count,
            "reviews": reviews,
        }
    )

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(
            user=request.user, recipe=recipe, is_deleted=False
        )
        user_bookmarks = Bookmark.objects.filter(
            user=request.user, recipe=recipe, is_deleted=False
        )
        user_reviews = Review.objects.filter(
            user=request.user, recipe=recipe, is_deleted=False
        )

        context.update(
            {
                "is_liked": user_likes.exists(),
                "is_bookmarked": user_bookmarks.exists(),
                "has_review": user_reviews.exists(),
                "user_review": user_reviews.first(),
            }
        )

    return render(request, "appRecipe/recipe_view.html", context=context)


def category_view(request, slug):
    context = get_common_context()

    category = get_object_or_404(Category, slug=slug, is_deleted=False)

    recipes = Recipe.objects.filter(
        category=category, author__is_deleted=False, is_deleted=False
    ).annotate(like_count=Count("like"))
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
            "category": category,
        }
    )
    return render(request, "appRecipe/category_view.html", context=context)


@login_required
def create_recipe(request):
    context = get_common_context()
    if request.method == "POST":
        form = RecipeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            base_slug = slugify(recipe.name)
            unique_slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            recipe.slug = unique_slug
            recipe.save()
            messages.success(request, "Recipe has been created!")
            return redirect("recipe-view", slug=recipe.slug)
        else:
            messages.error(request, form.errors)
    else:
        form = RecipeCreateForm()
    context.update({"title": "Create Recipe | Recime", "form": form})
    return render(request, "appRecipe/create_recipe.html", context)


@login_required
def update_recipe(request, slug):
    recipe = get_object_or_404(
        Recipe, slug=slug, author=request.user, author__is_deleted=False
    )
    context = get_common_context()

    if request.method == "POST":
        fields_updated = []

        name = request.POST.get("name")
        category_id = request.POST.get("category")
        about = request.POST.get("about")
        ingredients = request.POST.get("ingredients")
        preparation = request.POST.get("preparation")

        if name and name != recipe.name:
            recipe.name = name
            base_slug = slugify(recipe.name)
            unique_slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            recipe.slug = unique_slug
            fields_updated.append("Name and Slug")

        if category_id and category_id != str(recipe.category_id):
            recipe.category_id = category_id
            fields_updated.append("Category")

        if about and about != recipe.about:
            recipe.about = about
            fields_updated.append("About")

        if ingredients and ingredients != recipe.ingredients:
            recipe.ingredients = ingredients
            fields_updated.append("Ingredients")

        if preparation and preparation != recipe.preparation:
            recipe.preparation = preparation
            fields_updated.append("Preparation")

        if fields_updated:
            recipe.save()
            messages.success(
                request,
                f"Recipe updated successfully! Updated fields: {', '.join(fields_updated)}",
            )
            return redirect("user_settings")
        else:
            messages.info(request, "No changes were made to the recipe.")

        return redirect("user_settings")

    context.update({"title": "Update Recipe | Recime", "recipe": recipe})
    return render(request, "appRecipe/update_recipe.html", context)


@login_required
def remove_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)

    if request.method == "POST":
        recipe.is_deleted = True
        unique_slug = f"{recipe.slug}_{datetime.now()}_deleted"
        counter = 1
        while Recipe.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{recipe.slug}_{datetime.now()}_{counter}_deleted"
            counter += 1
        recipe.slug = unique_slug
        recipe.save()
        messages.success(request, "Recipe has been removed!")
        return redirect("settings_my_recipes")

    return redirect("settings_my_recipes")
