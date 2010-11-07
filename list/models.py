from django.db import models

from food.models import Ingredient
from planning.models import Meal
from django.db.models import permalink

class ShoppingList(models.Model):
    date = models.DateField()
    extra_ingredients = models.ManyToManyField(Ingredient, through='ExtraIngredient', related_name='extra_in_lists')
    not_needed_ingredients = models.ManyToManyField(Ingredient, through='NotNeededIngredient',
                                                    related_name='not_needed_in_lists')

    def __unicode__(self):
        return str(self.date)

    @permalink
    def get_absolute_url(self):
        return ('list.views.detail', [str(self.id)])

class ExtraIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList)
    amount = models.FloatField()
    ingredient = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return '%s %s %s'%(self.amount, self.ingredient.unit, self.ingredient)


class NotNeededIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList)
    amount = models.FloatField()
    ingredient = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return '%s %s %s'%(self.amount, self.ingredient.unit, self.ingredient)