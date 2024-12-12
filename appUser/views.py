from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from appRecipe.models import Recipe
from appRecipe.views import get_common_context
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


@login_required
def settings(request):
    context = get_common_context()
    user = request.user
    context.update({"user": user, "title": f"{user.username} | Settings"})
    return render(request, "appUser/settings.html", context=context)
