from food.models import *
from food.forms import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template.context import RequestContext
from django.forms.models import inlineformset_factory
from food.utils import get_ingredient_amount_from_string
from django.contrib import messages


def recipe_edit(request, id):
    IngredientFormset = inlineformset_factory(Recipe, Containment)

    recipe = get_object_or_404(Recipe, pk=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        formset = IngredientFormset(request.POST, instance=recipe)
        if form.is_valid() and formset.is_valid():
            recipe = form.save()
            formset.save()
            messages.success(request, 'Recipe updated.')
            return redirect(recipe_edit, id=recipe.id)

    else:
        form = RecipeForm(instance=recipe)
        formset = IngredientFormset(instance=recipe)

    dict = {
        'recipe': recipe,
        'form': form,
        'formset': formset,
    }
    return render_to_response('food/recipe_edit.html',
                              dict,
                              context_instance=RequestContext(request))


def recipe_ingredient_wizard(request, id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=id)
        if 'save' in request.GET:
            result_formset = HiddenIngredientAmountFormset(request.POST)
            erase = ErasePreviousIngredientsForm(request.POST)
            if not result_formset.is_valid() or not erase.is_valid():
                raise Exception('Did you just feed me with crappy input ?')
            if erase.cleaned_data['erase']:
                recipe.containment_set.all().delete()
            for ia in result_formset.cleaned_data:
                # Adding the ingredient to the recipe
                ingredient = Ingredient.objects.get(pk=ia['ingredient'])
                c, created = Containment.objects.get_or_create(ingredient=ingredient,
                                                      recipe=recipe,
                                                      defaults={'amount': 0})
                c.amount += float(ia['amount'])
                c.save()
            messages.success(request, 'Ingredients updated.')
            return redirect(recipe)
        else:
            form = IngredientWizardForm(request.POST)
            if form.is_valid():
                result = [get_ingredient_amount_from_string(line) for line in form.cleaned_data['ingredients'].split('\n') if line]
                result_formset = HiddenIngredientAmountFormset(
                        initial =[{ 'amount':ia.amount,
                                    'ingredient':ia.ingredient.id }
                                  for ia in result if ia.__class__ is IngredientAmount])
                erase = ErasePreviousIngredientsForm()
                ingredients_to_erase = recipe.containment_set.all().select_related('ingredient')

                return render_to_response('food/recipe_ingredient_wizard.html', {
                    'form': form,
                    'result':result,
                    'result_formset': result_formset,
                    'erase':erase,
                    'ingredients_to_erase':ingredients_to_erase
                    },
                                          context_instance=RequestContext(request))

    else:
        form = IngredientWizardForm()

    return render_to_response('food/recipe_ingredient_wizard.html', {
        'form': form,
        },
                              context_instance=RequestContext(request))
