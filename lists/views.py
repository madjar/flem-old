import hashlib
from django.template.context import RequestContext
from django.contrib import messages
from lists.forms import ListCreateForm
from models import ShoppingList
from food.models import Containment

from django.shortcuts import render_to_response, get_object_or_404, redirect
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

    return render_to_response('lists/detail.html', {'list': shopping_list, 'ingredients': ingredients})


def create(request):
    already_assigned_meals = None
    if request.method == 'POST':
        form = ListCreateForm(request.POST)
        if form.is_valid():
            shopping_list = None
            try:
                from_date = form.cleaned_data['from_date']
                to_date = form.cleaned_data['to_date']
                date = form.cleaned_data['date']
                shopping_list = ShoppingList.create_for_range(from_date,
                                                              to_date)
                shopping_list.date = date
                shopping_list.save()
            except ShoppingList.RangeNotEmptyException as e:
                override_hash = hashlib.sha1('%s%s%s'%(date.ctime(),
                                                       from_date.ctime(),
                                                       to_date.ctime())
                                             ).hexdigest()
                if form.cleaned_data['override'] == override_hash:
                    shopping_list = ShoppingList.create_for_range(from_date,
                                                                  to_date,
                                                                  override=True)
                    shopping_list.date = date
                    shopping_list.save()
                else:
                    form.data = form.data.copy()
                    form.data['override'] = override_hash
                    already_assigned_meals = e[0].select_related('shopping_list')

            if shopping_list:
                messages.success(request, 'Shopping list created updated.')
                return redirect(shopping_list)

    else:
        form = ListCreateForm()

    dict = {
        'form': form,
        'already_assigned_meals': already_assigned_meals,
    }
    return render_to_response('lists/create.html',
                              dict,
                              context_instance=RequestContext(request))
