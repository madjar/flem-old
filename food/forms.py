from food.models import *
from django.forms.models import ModelForm

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('ingredients',)

