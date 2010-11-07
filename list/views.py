from models import ShoppingList
from food.models import Containment, Recipe

from django.shortcuts import render_to_response, get_object_or_404


def detail(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)
    ingredients = list(shopping_list.extraingredient_set.all())

    for meal in shopping_list.meals.all().only('id', 'persons'):
        ingredients_amounts = Containment.objects.all().filter(recipe__in=meal.recipes.all().values('id').query)
        for ia in ingredients_amounts:
            ingredients.append(ia*meal.persons)


    ingredients.sort(cmp=lambda x,y: cmp(x.section.position,y.section.position) or cmp(x.name,y.name),
                     key=lambda x: x.ingredient
                     )


    return render_to_response('list/detail.html', {'list': shopping_list, 'ingredients': ingredients})

