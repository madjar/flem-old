import datetime
import itertools
from django.db import models
from food.models import Ingredient, IngredientAmount
from django.db.models import permalink
from planning.models import Meal
from lists.utils import date_range


class ShoppingList(models.Model):
    date = models.DateField()
    extra_ingredients = models.ManyToManyField(Ingredient, through='ExtraIngredient', related_name='extra_in_lists')
    not_needed_ingredients = models.ManyToManyField(Ingredient, through='NotNeededIngredient',
                                                    related_name='not_needed_in_lists')

    def __unicode__(self):
        return str(self.date)

    @permalink
    def get_absolute_url(self):
        return 'lists.views.detail', [str(self.id)]

    class RangeNotEmptyException(Exception):
        pass

    @staticmethod
    def create_for_range(date_from, date_to, moment_from='L', moment_to='D', override=False):
        existing_meals = Meal.objects.filter(date__range=(date_from, date_to))

        moments = itertools.product(date_range(date_from, date_to + datetime.timedelta(days=1)),
                                    ('L', 'D'))

        if moment_from == 'D':
            # If we must not include the lunch of the first day
            moments = itertools.islice(moments, 1, None)
            existing_meals.exclude(date=date_from, time_of_day='L')

        if moment_to == 'L':
            # If we do not include the dinner of the last day
            moments = list(moments)[:-1]
            existing_meals.exclude(date=date_to, time_of_day='D')

        if existing_meals and not override:
                raise ShoppingList.RangeNotEmptyException(existing_meals.all())

        shopping_list = ShoppingList(date=datetime.date.today())
        shopping_list.save()

        if existing_meals and override:
            existing_meals.update(shopping_list=shopping_list)

        existing_moments = existing_meals.values_list('date', 'time_of_day')

        moments = itertools.ifilter(lambda x: x not in existing_moments, moments)

        # TODO find a way to create all those meals in a single query
        for date, time_of_day in moments:
            meal = Meal(date=date, time_of_day=time_of_day, persons=0, shopping_list=shopping_list)
            meal.save()

        return shopping_list


class ExtraIngredient(IngredientAmount):
    shopping_list = models.ForeignKey(ShoppingList)


class NotNeededIngredient(IngredientAmount):
    shopping_list = models.ForeignKey(ShoppingList)
