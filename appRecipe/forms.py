from ckeditor.widgets import CKEditorWidget
from django import forms

from appRecipe.models import Recipe


# from customUtils import BootstrapFormMixin


class RecipeCreateForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorWidget(), required=True)
    ingredients = forms.CharField(widget=CKEditorWidget(), required=True)
    preparation = forms.CharField(widget=CKEditorWidget(), required=True)

    class Meta:
        model = Recipe
        fields = ["name", "category", "image", "about", "ingredients", "preparation"]
