from ckeditor.widgets import CKEditorWidget
from django import forms

from appRecipe.models import Recipe
from customUtils import BootstrapFormMixin


class RecipeCreateForm(BootstrapFormMixin, forms.ModelForm):
    ingredients = forms.CharField(widget=CKEditorWidget(), required=True)
    preparation = forms.CharField(widget=CKEditorWidget(), required=True)

    class Meta:
        model = Recipe
        fields = ["name", "category", "image", "about", "ingredients", "preparation"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
        }
