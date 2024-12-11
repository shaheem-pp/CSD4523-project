from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from appRecipe.models import Recipe
from appUser.models import Like, Bookmark


@login_required
def toggle_like(request):
    print("called toggle_like")
    recipe_id = request.POST.get("recipe_id")
    recipe = Recipe.objects.get(id=recipe_id)

    # Check if the user has already liked the recipe
    like, created = Like.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:  # The user already liked the recipe, so remove the like
        like.delete()
        liked = False
    else:
        liked = True

    # Return the updated like count and liked status
    return JsonResponse({"like_count": recipe.like_set.count(), "liked": liked})


@login_required
def toggle_bookmark(request):
    print("called toggle_bookmark")
    recipe_id = request.POST.get("recipe_id")
    recipe = Recipe.objects.get(id=recipe_id)

    # Check if the user has already bookmarked the recipe
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:  # The user already bookmarked the recipe, so remove the bookmark
        bookmark.delete()
        bookmarked = False
    else:
        bookmarked = True

    # Return the updated bookmark status
    return JsonResponse({"bookmarked": bookmarked})
