from django.db import models

from food.models import Ingredient
from planning.models import Meal

class ShoppingList(models.Model):
    date = models.DateField(auto_now_add=True)
    extra_ingredients = models.ManyToManyField(Ingredient, through='ExtraIngredient', related_name='extra_in_lists')
    not_needed_ingredients = models.ManyToManyField(Ingredient, through='NotNeededIngredient',
                                                    related_name='not_needed_in_lists')

    def __unicode__(self):
        return str(self.date)


class ExtraIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.FloatField()

    def __unicode__(self):
        return '%s %s'%(self.amount, self.ingredient)


class NotNeededIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.FloatField()

    def __unicode__(self):
        return '%s %s'%(self.amount, self.ingredient)