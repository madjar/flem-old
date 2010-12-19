from food.models import *
from food.forms import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template.context import RequestContext
from django.forms.models import inlineformset_factory, modelformset_factory

def recipe_edit(request, id):
    IngredientFormset = inlineformset_factory(Recipe, Containment)

    recipe = get_object_or_404(Recipe, pk=id)
    if request.method == 'POST': # If the form has been submitted...
        form = RecipeForm(request.POST, instance=recipe) # A form bound to the POST data
        formset = IngredientFormset(request.POST, instance=recipe)
        if form.is_valid() and formset.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            recipe = form.save()
            formset.save()
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
