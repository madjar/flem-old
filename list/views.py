from models import ShoppingList
from food.models import Containment

from django.shortcuts import render_to_response, get_object_or_404
from collections import defaultdict, namedtuple
from operator import attrgetter

IngredientAmountTuple = namedtuple('IngredientAmountTuple', 'ingredient amount')
compareIngredientsPerSections = lambda x,y: cmp(x.section.position,y.section.position) or cmp(x.name,y.name)


def detail(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)

    ingredients_dict = defaultdict(float)

    # Add the extra ingredients
    for ia in shopping_list.extraingredient_set.all():
        ingredients_dict[ia.ingredient] += ia.amount

    # Remove those that aren't needed
    for ia in shopping_list.notneededingredient_set.all():
        ingredients_dict[ia.ingredient] -= ia.amount

    # Add the ingredients from the recipes
    for meal in shopping_list.meals.all().only('id', 'persons'):
        ingredients_amounts = Containment.objects.all().filter(recipe__in=meal.recipes.all().values('id').query)
        for ia in ingredients_amounts:
            ingredients_dict[ia.ingredient] += ia.amount * meal.persons

    # Then, we sort the ingredients per section before giving it to the view.
    ingredients = sorted((IngredientAmountTuple(k,v) for k, v in ingredients_dict.iteritems() if v != 0),
                         cmp=compareIngredientsPerSections,
                         key=attrgetter('ingredient')
                         )

    return render_to_response('list/detail.html', {'list': shopping_list, 'ingredients': ingredients})
