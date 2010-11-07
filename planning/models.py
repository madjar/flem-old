from django.db import models

from food.models import Recipe


class Meal(models.Model):
    TIMES_CHOICES = (
        ('M', 'Midday'),
        ('E', 'Evening'),
        ('O', 'Other'),
    )

    date = models.DateField()
    persons = models.IntegerField()
    time_of_day = models.CharField(max_length=1, choices=TIMES_CHOICES)
    recipes = models.ManyToManyField(Recipe)
    shopping_list = models.ForeignKey('list.ShoppingList', blank=True, related_name='meals')