from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from appRecipe.models import Recipe
from appRecipe.views import get_common_context
from appUser.models import Like, Bookmark, Review


@login_required
def toggle_like(request):
    recipe_id = request.POST.get("recipe_id")
    recipe = Recipe.objects.get(id=recipe_id)

    like, created = Like.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({"like_count": recipe.like_set.count(), "liked": liked})


@login_required
def toggle_bookmark(request):
    recipe_id = request.POST.get("recipe_id")
    recipe = Recipe.objects.get(id=recipe_id)

    bookmark, created = Bookmark.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:
        bookmark.delete()
        bookmarked = False
    else:
        bookmarked = True

    return JsonResponse({"bookmarked": bookmarked})


@login_required
def settings(request):
    context = get_common_context()
    user = request.user
    context.update({"user": user, "title": f"{user} | Settings"})
    return render(request, "appUser/settings.html", context=context)


@login_required
def add_review(request, recipe_slug):
    if request.method == "POST":

        recipe = get_object_or_404(Recipe, slug=recipe_slug, is_deleted=False)

        review_content = request.POST.get("review")
        if not review_content:
            return redirect("recipe-view", slug=recipe_slug)

        review = Review.objects.filter(user=request.user, recipe=recipe).first()

        if review:
            review.review = review_content
            review.save()
        else:
            Review.objects.create(
                user=request.user, recipe=recipe, review=review_content
            )

        return redirect("recipe-view", slug=recipe_slug)

    return redirect("recipe-view", slug=recipe_slug)


@login_required
def delete_review(request, recipe_slug):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, slug=recipe_slug, is_deleted=False)
        review = Review.objects.filter(user=request.user, recipe=recipe).first()

        if review:
            review.delete()

        return redirect("recipe-view", slug=recipe_slug)
    return redirect("recipe-view", slug=recipe_slug)


@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(author=request.user, is_deleted=False)
    response_data = [
        {
            "name": recipe.name,
            "about": recipe.about,
            "image": recipe.image.url,
        }
        for recipe in recipes
    ]
    response = {
        "type": "recipes",
        "items": response_data,
    }
    return JsonResponse(response, safe=False)


@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user, is_deleted=False)
    response_data = [
        {
            "recipe_name": bookmark.recipe.name,
            "recipe_slug": bookmark.recipe.slug,
            "recipe_image": bookmark.recipe.image.url,
        }
        for bookmark in bookmarks
    ]
    response = {
        "type": "bookmarks",
        "items": response_data,
    }
    return JsonResponse(response, safe=False)


@login_required
def my_likes(request):
    likes = Like.objects.filter(user=request.user, is_deleted=False).values(
        "recipe__id", "recipe__name", "recipe__about", "recipe__image"
    )
    response = {
        "type": "likes",
        "items": list(likes),
    }
    return JsonResponse(response, safe=False)


@login_required
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user, is_deleted=False)
    response_data = [
        {
            "recipe_name": review.recipe.name,
            "recipe_slug": review.recipe.slug,
            "review": review.review,
            "last_updated_on": datetime.strftime(review.updated_on, "%b %d, %Y"),
        }
        for review in reviews
    ]
    response = {
        "type": "reviews",
        "items": response_data,
    }
    return JsonResponse(response, safe=False)


@login_required
def chef_verify(request):
    VALID_CHEF_CODES = ["CHEF2024", "2G3COMPETITION", "TAJCH3"]
    if request.method == "POST":
        chefCodeInput = request.POST.get("chefCodeInput")
        if chefCodeInput in VALID_CHEF_CODES:
            user = request.user
            user.user_type = 3
            user.designation = ""
            user.save()
            messages.success(request, "You are verified as Chef!")
            return redirect("user_settings")
        else:
            messages.error(request, "Your chef code is not valid!")
            return redirect("user_settings")
    else:
        return redirect("user_settings")


@login_required
def update_user_details(request):
    try:
        user = request.user

        if request.method == "POST":
            name = request.POST.get("name")
            existing_password = request.POST.get("existing_password")
            new_password = request.POST.get("new_password")
            designation = request.POST.get("designation")
            image = request.FILES.get("image")

            fields_updated = False

            if name != user.name:
                user.name = name
                fields_updated = True

            if existing_password and new_password:
                if not user.check_password(existing_password):
                    return redirect("update_user_details")

                if existing_password == new_password:
                    new_password = None
                else:
                    user.set_password(new_password)
                    fields_updated = True

                    user = authenticate(
                        request, email=user.email, password=new_password
                    )
                    if user is not None:
                        login(request, user)
                        messages.success(
                            request,
                            "Password changed successfully and re-authenticated!",
                        )
                    else:
                        return redirect("update_user_details")

            if image:
                user.image = image
                fields_updated = True

            if user.user_type == 3 and designation != user.designation:
                user.designation = designation
                fields_updated = True
            elif user.user_type != 3:
                user.designation = None
                fields_updated = True

            if fields_updated:
                user.save()
                messages.success(request, "User details updated successfully!")
                return redirect("user_settings")
            else:
                messages.info(request, "No changes detected.")
                return redirect("user_settings")

    except ValidationError as e:
        messages.error(request, f"Error: {e.message}")
        return redirect("user_settings")
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect("user_settings")

    return redirect("user_settings")
