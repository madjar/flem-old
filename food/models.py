from django.db import models
from django.db.models import permalink

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
        return ('recipe_view', [str(self.id)])

class Containment(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.FloatField()
