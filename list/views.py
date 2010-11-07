from models import ShoppingList

from django.shortcuts import render_to_response, get_object_or_404


def detail(request, list_id):
    l = get_object_or_404(ShoppingList, pk=list_id)
    ingredients = list(l.extraingredient_set.all())

    ingredients.sort(key=lambda i: i.ingredient.name, reverse=True)
    ingredients.sort(key=lambda i: i.ingredient.section.position)


    return render_to_response('list/detail.html', {'list': l, 'ingredients': ingredients})