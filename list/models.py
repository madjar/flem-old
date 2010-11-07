from django.db import models

from food.models import Ingredient, IngredientAmount
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

class ExtraIngredient(IngredientAmount):
    shopping_list = models.ForeignKey(ShoppingList)


class NotNeededIngredient(IngredientAmount):
    shopping_list = models.ForeignKey(ShoppingList)