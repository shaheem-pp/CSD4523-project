from django.shortcuts import render

from appRecipe.models import Category


# Create your views here.


def home(request):
    categories = Category.objects.filter(is_deleted=False)
    context = {"title": "Recime | The Recipe App", "categories": categories}
    return render(request, "appRecipe/home.html", context=context)
