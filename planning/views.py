from planning.models import Meal
from food.models import Recipe

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

import datetime


def range(request, year_from, month_from, day_from, year_to, month_to, day_to):
    date_from = datetime.date(int(year_from), int(month_from), int(day_from))
    date_to = datetime.date(int(year_to), int(month_to), int(day_to))

    meals = Meal.objects.filter(date__range=(date_from, date_to))

    return render_to_response('planning/range.html', {'meals': meals, 'from': date_from, 'to': date_to})


def update(request):
    if request.is_ajax():
        new_planning = simplejson.loads(request.POST['new_planning'])

        meals = Meal.objects.filter(id__in=new_planning.keys()).only('id').all()
        Meal.recipes.through.objects.filter(meal__id__in=new_planning.keys()).delete()
        for meal in meals:
            recipe_ids = new_planning[str(meal.id)]
            recipes = Recipe.objects.filter(id__in=recipe_ids).only('id').all()
            for recipe in recipes:
                Meal.recipes.through(meal=meal, recipe=recipe).save()

        return HttpResponse("OK", mimetype="text/plain")
    else:
        return HttpResponse(status=400)
