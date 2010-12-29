from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import floatformat

class Section(models.Model):
    """Where you can find it in your supermarket"""
    name = models.CharField(max_length=64)
    position = models.IntegerField()

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=64, blank=True)
    is_food = models.BooleanField()
    section = models.ForeignKey(Section)

    def __unicode__(self):
        if self.unit:
            return '%s (%s)'%(self.name, self.unit)
        else:
            return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'caterogy'
        verbose_name_plural = 'categories'

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category)
    ingredients = models.ManyToManyField(Ingredient, through='Containment')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('food.views.recipe_detail', [str(self.id)])


class IngredientAmount(models.Model):
    amount = models.FloatField()
    ingredient = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return '%s %s %s'%(floatformat(self.amount), self.ingredient.unit, self.ingredient.name)

    class Meta:
        abstract = True

class Containment(IngredientAmount):
    recipe = models.ForeignKey(Recipe)
