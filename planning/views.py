from planning.models import Meal

from django.shortcuts import render_to_response

import datetime

def range(request, year_from, month_from, day_from, year_to, month_to, day_to):
    date_from = datetime.date(int(year_from), int(month_from), int(day_from))
    date_to = datetime.date(int(year_to), int(month_to), int(day_to))

    meals = Meal.objects.filter(date__range=(date_from, date_to))

    return render_to_response('planning/range.html', {'meals': meals, 'from': date_from, 'to': date_to})