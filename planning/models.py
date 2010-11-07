from django.db import models

from food.models import Recipe


class Meal(models.Model):
    TIMES_CHOICES = (
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('O', 'Other'),
    )

    date = models.DateField()
    time_of_day = models.CharField(max_length=1, choices=TIMES_CHOICES)
    persons = models.IntegerField()
    recipes = models.ManyToManyField(Recipe)
    shopping_list = models.ForeignKey('list.ShoppingList', blank=True, related_name='meals')

    def __unicode__(self):
        return '%s %s'%(self.get_time_of_day_display(), self.date)
