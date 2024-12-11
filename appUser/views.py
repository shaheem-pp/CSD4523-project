from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from appRecipe.models import Recipe
from appUser.models import Like, Bookmark


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
