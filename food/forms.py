from food.models import *
from django.forms.models import ModelForm
from django import forms
from django.forms.formsets import formset_factory

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('ingredients',)


class IngredientWizardForm(forms.Form):
    ingredients = forms.CharField(widget=forms.widgets.Textarea)


class HiddenIngredientAmountForm(forms.Form):
    ingredient = forms.CharField(widget=forms.widgets.HiddenInput)
    amount = forms.CharField(widget=forms.widgets.HiddenInput)

HiddenIngredientAmountFormset = formset_factory(HiddenIngredientAmountForm, extra=0)

class ErasePreviousIngredientsForm(forms.Form):
    erase = forms.BooleanField(required=False, label='Erase current ingredients')
